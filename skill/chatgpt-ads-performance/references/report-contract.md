# Reporting contract

## Contents

1. Executive verdict
2. Data-quality block
3. KPI scorecard
4. Findings
5. Action register
6. Monitoring checkpoint
7. Language rules

## 1. Executive verdict

Open with one of:

- healthy and scalable
- healthy but constrained
- mixed; optimization needed
- inefficient with reliable evidence
- not assessable because data is insufficient
- not assessable because tracking is broken
- operational incident

Add one sentence explaining the binding constraint.

## 2. Data-quality block

Always state:

- period and timezone
- comparison period
- account currency
- click attribution window
- view attribution window
- attribution time basis
- incomplete days excluded or included
- conversion source
- data freshness
- known tracking limitations

Rate data quality:

- green: complete and aligned
- amber: delayed, partial, or missing business value
- red: broken, duplicated, or incomparable

## 3. KPI scorecard

Use a table:

| KPI | Current | Previous | Change | Target | Status | Evidence |
|---|---:|---:|---:|---:|---|---|
| Spend | | | | | | |
| Impressions | | | | | | |
| Clicks | | | | | | |
| CTR | | | | | | |
| CPC | | | | | | |
| Conversions | | | | | | |
| CVR | | | | | | |
| CPA | | | | | | |
| Revenue | | | | | | |
| ROAS | | | | | | |

Omit unavailable metrics rather than filling zero. Label currency in every monetary column or heading.

## 4. Findings

Separate:

### Observed facts

Directly returned or calculated from data.

### Inferences

Likely explanations with confidence and alternatives.

### Risks

Spend, policy, tracking, delivery, attribution, or business risks.

### Opportunities

Only opportunities that are supported by evidence and can be acted on.

For entity tables include:

- ID and name
- spend
- clicks
- conversions
- CPA or ROAS
- status
- evidence
- diagnosis

## 5. Action register

| Priority | Object | Action | Why | Expected effect | Confidence | Risk | Approval | Review | Rollback |
|---|---|---|---|---|---|---|---|---|---|

Use:

- P0: contain an active incident
- P1: high business impact
- P2: meaningful optimization
- P3: test or backlog

Include a "do not change yet" list to prevent premature optimization.

## 6. Monitoring checkpoint

End with:

- changes since last check
- open experiments
- next valid decision date
- alert thresholds
- exact next check

If no material change exists, say so and preserve the prior plan.

## 7. Language rules

- Respond in the user's language.
- Lead with outcome, not tool activity.
- Define specialized metrics once.
- Separate platform conversion from customer acquisition.
- Never say "significant" unless statistical or business significance is established.
- Never say a change "worked" immediately after applying it.
- Use exact dates, not only "today" or "last week."
- Make unavailable information visible.

