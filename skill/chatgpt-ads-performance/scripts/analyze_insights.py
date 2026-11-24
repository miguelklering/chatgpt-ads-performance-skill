#!/usr/bin/env python3
"""Calculate and classify ChatGPT Ads insight metrics from JSON or CSV.

The script is deliberately API-tolerant: it accepts rows directly, a JSON
object with a data/results/rows list, or CSV. It never invents missing
metrics. Use --prior for an equivalent comparison period.
"""

from __future__ import annotations

import argparse
import csv
import json
import math
import sys
from collections import defaultdict
from pathlib import Path
from typing import Any, Iterable


NUMERIC_ALIASES = {
    "impressions": ("impressions", "ad_impressions"),
    "clicks": ("clicks", "ad_clicks"),
    "spend": ("spend", "amount_spent", "cost"),
    "conversions": (
        "conversions",
        "click_through_conversions",
        "goal_conversions",
        "attributed_conversions",
        "purchases",
    ),
    "revenue": (
        "revenue",
        "conversion_value",
        "purchase_value",
        "attributed_revenue",
        "value",
    ),
}


def parse_number(value: Any) -> float | None:
    if value is None or value == "":
        return None
    if isinstance(value, bool):
        return float(value)
    if isinstance(value, (int, float)):
        return float(value)
    text = str(value).strip().replace(",", "")
    if text.endswith("%"):
        text = text[:-1]
    try:
        return float(text)
    except ValueError:
        return None


def flatten(value: Any, prefix: str = "") -> dict[str, Any]:
    output: dict[str, Any] = {}
    if isinstance(value, dict):
        for key, item in value.items():
            name = f"{prefix}.{key}" if prefix else str(key)
            output.update(flatten(item, name))
    else:
        output[prefix] = value
    return output


def load_rows(path: Path) -> list[dict[str, Any]]:
    if not path.exists():
        raise FileNotFoundError(path)
    if path.suffix.lower() == ".csv":
        with path.open(newline="", encoding="utf-8-sig") as handle:
            return [dict(row) for row in csv.DictReader(handle)]

    with path.open(encoding="utf-8") as handle:
        payload = json.load(handle)
    if isinstance(payload, list):
        rows = payload
    elif isinstance(payload, dict):
        rows = None
        for key in ("data", "results", "rows", "items"):
            if isinstance(payload.get(key), list):
                rows = payload[key]
                break
        if rows is None:
            rows = [payload]
    else:
        raise ValueError("Expected a JSON object, JSON list, or CSV file")
    return [row for row in rows if isinstance(row, dict)]


def find_value(row: dict[str, Any], aliases: Iterable[str]) -> Any:
    flat = flatten(row)
    lowered = {key.lower(): value for key, value in flat.items()}
    for alias in aliases:
        alias_lower = alias.lower()
        if alias_lower in lowered:
            return lowered[alias_lower]
        for key, value in lowered.items():
            if key.rsplit(".", 1)[-1] == alias_lower:
                return value
    return None


def entity_value(row: dict[str, Any], field: str) -> str:
    flat = flatten(row)
    if field in flat:
        return str(flat[field])
    for key, value in flat.items():
        if key.rsplit(".", 1)[-1] == field:
            return str(value)
    return ""


def group_rows(rows: list[dict[str, Any]], group_by: list[str]) -> dict[str, dict[str, Any]]:
    grouped: dict[str, dict[str, Any]] = defaultdict(
        lambda: {
            "impressions": 0.0,
            "clicks": 0.0,
            "spend": 0.0,
            "conversions": 0.0,
            "revenue": 0.0,
            "_present": set(),
            "_rows": 0,
        }
    )
    for index, row in enumerate(rows):
        parts = [entity_value(row, field) for field in group_by]
        if not any(parts):
            parts = [
                entity_value(row, "entity_id")
                or entity_value(row, "id")
                or entity_value(row, "name")
                or f"row-{index + 1}"
            ]
        key = " | ".join(part or "(blank)" for part in parts)
        item = grouped[key]
        item["entity"] = key
        item["_rows"] += 1
        for metric, aliases in NUMERIC_ALIASES.items():
            number = parse_number(find_value(row, aliases))
            if number is not None:
                item[metric] += number
                item["_present"].add(metric)
    return dict(grouped)


def safe_div(numerator: float, denominator: float) -> float | None:
    if denominator == 0:
        return None
    return numerator / denominator


def wilson_interval(successes: float, trials: float, z: float = 1.96) -> tuple[float, float] | None:
    if trials <= 0 or successes < 0 or successes > trials:
        return None
    p = successes / trials
    denominator = 1 + z * z / trials
    center = (p + z * z / (2 * trials)) / denominator
    margin = (
        z
        * math.sqrt((p * (1 - p) + z * z / (4 * trials)) / trials)
        / denominator
    )
    return max(0.0, center - margin), min(1.0, center + margin)


def evidence_label(clicks: float, conversions: float) -> str:
    if clicks < 30 or conversions < 3:
        return "insufficient"
    if clicks < 100 or conversions < 10:
        return "directional"
    return "decision-ready"


def classify(
    metrics: dict[str, Any],
    target_cpa: float | None,
    target_roas: float | None,
    min_clicks: int,
    min_conversions: int,
) -> tuple[str, list[str]]:
    clicks = metrics["clicks"]
    spend = metrics["spend"]
    conversions = metrics["conversions"]
    cpa = metrics["cpa"]
    roas = metrics["roas"]
    available = set(metrics.get("available_metrics", []))
    flags: list[str] = []

    if metrics["impressions"] == 0:
        return "insufficient-data", ["zero-impressions"]
    if target_cpa is not None and "conversions" not in available:
        return "tracking-risk", ["missing-conversion-field"]
    if target_roas is not None and "revenue" not in available:
        return "tracking-risk", ["missing-revenue-field"]
    if clicks >= 20 and conversions == 0:
        flags.append("tracking-or-conversion-risk")
    if target_cpa and conversions == 0 and spend >= 2 * target_cpa:
        flags.append("spend-above-2x-target-without-conversion")
    if clicks < min_clicks or conversions < min_conversions:
        return ("tracking-risk" if flags else "insufficient-data"), flags

    cpa_pass = target_cpa is None or (cpa is not None and cpa <= target_cpa)
    roas_pass = target_roas is None or (roas is not None and roas >= target_roas)

    if target_cpa is None and target_roas is None:
        return "watch", flags
    if cpa_pass and roas_pass:
        flags.append("scale-candidate")
        return "healthy", flags

    if target_cpa and cpa is not None and cpa > target_cpa * 1.3:
        flags.append("cpa-materially-above-target")
    if target_roas and roas is not None and roas < target_roas * 0.8:
        flags.append("roas-materially-below-target")
    return "inefficient", flags


def enrich(
    item: dict[str, Any],
    target_cpa: float | None,
    target_roas: float | None,
    min_clicks: int,
    min_conversions: int,
) -> dict[str, Any]:
    present = item.pop("_present")
    item.pop("_rows", None)

    impressions = item["impressions"]
    clicks = item["clicks"]
    spend = item["spend"]
    conversions = item["conversions"]
    revenue = item["revenue"]

    metrics = dict(item)
    metrics["ctr"] = safe_div(clicks, impressions)
    metrics["cpc"] = safe_div(spend, clicks)
    metrics["cpm"] = safe_div(spend * 1000, impressions)
    metrics["cvr"] = safe_div(conversions, clicks)
    metrics["cpa"] = safe_div(spend, conversions)
    metrics["roas"] = safe_div(revenue, spend) if "revenue" in present else None
    metrics["revenue_per_click"] = (
        safe_div(revenue, clicks) if "revenue" in present else None
    )
    interval = wilson_interval(conversions, clicks)
    metrics["cvr_ci95_low"] = interval[0] if interval else None
    metrics["cvr_ci95_high"] = interval[1] if interval else None
    metrics["evidence"] = evidence_label(clicks, conversions)
    metrics["available_metrics"] = sorted(present)
    status, flags = classify(
        metrics, target_cpa, target_roas, min_clicks, min_conversions
    )
    metrics["status"] = status
    metrics["flags"] = flags
    return metrics


def summarize(rows: list[dict[str, Any]]) -> dict[str, float]:
    result = {metric: 0.0 for metric in NUMERIC_ALIASES}
    for row in rows:
        for metric in result:
            result[metric] += float(row.get(metric) or 0)
    return result


def percent_change(current: float | None, prior: float | None) -> float | None:
    if current is None or prior in (None, 0):
        return None
    return (current - prior) / abs(prior)


def comparison(current: dict[str, Any], prior: dict[str, Any] | None) -> dict[str, Any]:
    if not prior:
        return {}
    output: dict[str, Any] = {}
    for metric in ("impressions", "clicks", "spend", "conversions", "revenue"):
        output[metric] = percent_change(current.get(metric), prior.get(metric))
    for metric in ("ctr", "cpc", "cpm", "cvr", "cpa", "roas"):
        output[metric] = percent_change(current.get(metric), prior.get(metric))
    return output


def fmt_number(value: float | None, decimals: int = 2) -> str:
    if value is None:
        return "—"
    return f"{value:,.{decimals}f}"


def fmt_percent(value: float | None) -> str:
    if value is None:
        return "—"
    return f"{value * 100:.2f}%"


def render_markdown(
    report: dict[str, Any], currency: str, target_cpa: float | None, target_roas: float | None
) -> str:
    lines = [
        "# ChatGPT Ads performance analysis",
        "",
        f"- Currency: {currency}",
        f"- Target CPA: {fmt_number(target_cpa)} {currency}" if target_cpa else "- Target CPA: not provided",
        f"- Target ROAS: {fmt_number(target_roas)}x" if target_roas else "- Target ROAS: not provided",
        "",
        "| Entity | Spend | Impr. | Clicks | CTR | CPC | Conv. | CVR | CPA | ROAS | Evidence | Status |",
        "|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|",
    ]
    for row in report["entities"]:
        lines.append(
            "| {entity} | {spend} {currency} | {impressions} | {clicks} | {ctr} | "
            "{cpc} {currency} | {conversions} | {cvr} | {cpa} {currency} | "
            "{roas} | {evidence} | {status} |".format(
                entity=row["entity"].replace("|", "/"),
                spend=fmt_number(row["spend"]),
                currency=currency,
                impressions=fmt_number(row["impressions"], 0),
                clicks=fmt_number(row["clicks"], 0),
                ctr=fmt_percent(row["ctr"]),
                cpc=fmt_number(row["cpc"]),
                conversions=fmt_number(row["conversions"], 0),
                cvr=fmt_percent(row["cvr"]),
                cpa=fmt_number(row["cpa"]),
                roas=(f"{row['roas']:.2f}x" if row["roas"] is not None else "—"),
                evidence=row["evidence"],
                status=row["status"],
            )
        )
    flagged = [row for row in report["entities"] if row["flags"]]
    if flagged:
        lines += ["", "## Flags", ""]
        for row in flagged:
            lines.append(f"- {row['entity']}: {', '.join(row['flags'])}")
    return "\n".join(lines)


def build_report(args: argparse.Namespace) -> dict[str, Any]:
    current_rows = load_rows(args.input)
    grouped = group_rows(current_rows, args.group_by)
    entities = [
        enrich(item, args.target_cpa, args.target_roas, args.min_clicks, args.min_conversions)
        for item in grouped.values()
    ]
    entities.sort(key=lambda row: row["spend"], reverse=True)

    total_raw = summarize(entities)
    total_seed = {
        "entity": "TOTAL",
        **total_raw,
        "_present": set().union(
            *(set(row["available_metrics"]) for row in entities)
        ),
        "_rows": len(entities),
    }
    total = enrich(
        total_seed, args.target_cpa, args.target_roas, args.min_clicks, args.min_conversions
    )

    prior_total = None
    if args.prior:
        prior_grouped = group_rows(load_rows(args.prior), args.group_by)
        prior_entities = [
            enrich(item, args.target_cpa, args.target_roas, args.min_clicks, args.min_conversions)
            for item in prior_grouped.values()
        ]
        prior_raw = summarize(prior_entities)
        prior_seed = {
            "entity": "TOTAL",
            **prior_raw,
            "_present": set().union(
                *(set(row["available_metrics"]) for row in prior_entities)
            ),
            "_rows": len(prior_entities),
        }
        prior_total = enrich(
            prior_seed,
            args.target_cpa,
            args.target_roas,
            args.min_clicks,
            args.min_conversions,
        )

    return {
        "currency": args.currency,
        "group_by": args.group_by,
        "targets": {"cpa": args.target_cpa, "roas": args.target_roas},
        "thresholds": {
            "min_clicks": args.min_clicks,
            "min_conversions": args.min_conversions,
        },
        "total": total,
        "prior_total": prior_total,
        "total_change": comparison(total, prior_total),
        "entities": entities,
    }


def self_test() -> int:
    rows = [
        {
            "entity_id": "good",
            "impressions": 10000,
            "clicks": 200,
            "spend": 400,
            "conversions": 20,
            "revenue": 1600,
        },
        {
            "entity_id": "weak",
            "impressions": 5000,
            "clicks": 100,
            "spend": 500,
            "conversions": 5,
            "revenue": 300,
        },
    ]
    grouped = group_rows(rows, ["entity_id"])
    enriched = [
        enrich(item, 30, 2.0, 30, 3) for item in grouped.values()
    ]
    by_name = {row["entity"]: row for row in enriched}
    assert by_name["good"]["status"] == "healthy"
    assert by_name["weak"]["status"] == "inefficient"
    assert round(by_name["good"]["ctr"], 4) == 0.02
    assert round(by_name["good"]["cpa"], 2) == 20.00
    assert round(by_name["good"]["roas"], 2) == 4.00
    missing_revenue = enrich(
        {
            "entity": "missing-revenue",
            "impressions": 10000.0,
            "clicks": 200.0,
            "spend": 400.0,
            "conversions": 20.0,
            "revenue": 0.0,
            "_present": {"impressions", "clicks", "spend", "conversions"},
            "_rows": 1,
        },
        30,
        2.0,
        30,
        3,
    )
    assert missing_revenue["status"] == "tracking-risk"
    assert "missing-revenue-field" in missing_revenue["flags"]
    print("Self-test passed")
    return 0


def parser() -> argparse.ArgumentParser:
    result = argparse.ArgumentParser(
        description="Analyze OpenAI Ads insight exports without inventing missing fields."
    )
    result.add_argument("input", nargs="?", type=Path, help="Current-period JSON or CSV")
    result.add_argument("--prior", type=Path, help="Equivalent prior-period JSON or CSV")
    result.add_argument(
        "--group-by",
        default="entity_id",
        help="Comma-separated grouping fields; default: entity_id",
    )
    result.add_argument("--currency", default="USD")
    result.add_argument("--target-cpa", type=float)
    result.add_argument("--target-roas", type=float)
    result.add_argument("--min-clicks", type=int, default=30)
    result.add_argument("--min-conversions", type=int, default=3)
    result.add_argument("--format", choices=("json", "markdown"), default="markdown")
    result.add_argument("--output", type=Path)
    result.add_argument("--self-test", action="store_true")
    return result


def main() -> int:
    args = parser().parse_args()
    if args.self_test:
        return self_test()
    if not args.input:
        print("input is required unless --self-test is used", file=sys.stderr)
        return 2
    args.group_by = [field.strip() for field in args.group_by.split(",") if field.strip()]
    try:
        report = build_report(args)
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1

    if args.format == "json":
        rendered = json.dumps(report, ensure_ascii=False, indent=2, sort_keys=True)
    else:
        rendered = render_markdown(
            report, args.currency, args.target_cpa, args.target_roas
        )
    if args.output:
        args.output.write_text(rendered + "\n", encoding="utf-8")
    else:
        print(rendered)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
