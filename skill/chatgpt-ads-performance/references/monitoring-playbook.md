# Monitoring playbook

## Contents

1. Monitoring modes
2. Launch cadence
3. Steady-state cadence
4. Incident checks
5. Alert thresholds
6. Checkpoint format

## 1. Monitoring modes

A skill invocation performs one monitoring cycle. Continuous monitoring requires an external scheduler or automation.

Choose:

- launch watch: first seven days
- steady-state: established campaigns
- experiment watch: active test with a decision date
- incident watch: suspected spend, serving, or tracking problem
- executive review: weekly or monthly business summary

## 2. Launch cadence

### Before activation

Verify:

- approved account and payment
- spend fuse
- correct currency, timezone, geography, and platforms
- campaign end date
- landing 200 for browser and OAI-AdsBot
- oppref survives redirects
- Pixel/CAPI and event linkage
- policy preflight
- paused hierarchy and approved creatives

### First two hours

Check configuration and critical errors, not performance:

- hierarchy active as intended
- no rejection or serving issue
- no wrong geography
- no abnormal spend
- landing available

### First complete day

Check:

- impressions and spend began
- budget pace
- clicks and CPC
- conversion events arriving
- no duplicate or malformed values

Do not judge CPA from incomplete attribution.

### 48–72 hours

Check:

- delivery constraint
- bid_too_low
- directional CTR and CPC
- tracking stability
- early CVR only as directional

### Day seven

Review ad groups, ads, platform, geography, conversion quality, and experiment integrity. Make changes only when evidence and business risk justify them.

## 3. Steady-state cadence

### Daily operational check

- account and payment
- spend fuse and budget pace
- review and serving issues
- zero-delivery anomalies
- landing availability
- conversion-event continuity

Keep the output short when no material change exists.

### Weekly performance review

- current seven days versus prior seven days
- rolling 28-day context
- campaign, ad-group, and ad economics
- platform, country, device, or product mix
- experiments reaching decision thresholds
- change log and post-change impact
- ranked action register

### Monthly strategy review

- spend, conversions, revenue, contribution, CPA/CAC, and ROAS
- marginal performance as spend changed
- lead or customer quality
- attribution sensitivity
- creative and context-hint learning
- forecast and budget allocation
- whether the channel still deserves experimental, maintenance, or growth status

## 4. Incident checks

Escalate immediately for:

- payment or account suspension
- spend limit missing where one is expected
- wrong market or currency
- unexpected budget or targeting change
- rejected ads across a material share of delivery
- active campaign with zero impressions after expected launch time
- spend without recorded clicks or conversions beyond normal freshness
- landing failure, redirect loss, robots block, or captcha
- conversion event outage
- duplicate conversion volume
- spend materially above approved pace

For every incident include:

- first observed time
- affected objects
- business impact
- current containment
- likely cause and evidence
- next diagnostic step
- write requiring approval

## 5. Alert thresholds

Use business-defined thresholds when available. Otherwise propose defaults and label them provisional.

Useful defaults:

- spend pace above plan by 20% after at least half the period has elapsed
- zero impressions for an approved active entity after 24 hours
- clicks with no conversion events when the site normally records events
- conversion count down more than 50% versus an equivalent period, with stable clicks
- CPA above target by 30% with decision-ready evidence
- ROAS below target by 20% with decision-ready evidence
- landing non-200 or oppref loss: immediate
- any wrong geography, payment issue, or policy rejection: immediate

Use both a relative and an absolute threshold to avoid noisy alerts on tiny numbers.

## 6. Checkpoint format

Record:

| Field | Value |
|---|---|
| Check time | Account timezone |
| Account | Name and currency |
| Scope | Campaigns or full account |
| Period | Complete dates |
| Attribution | Click, view, and time basis |
| Spend | Current and comparison |
| Conversions | Current and comparison |
| CPA/ROAS | Current and comparison |
| Data quality | Healthy, delayed, or broken |
| Incidents | Open/closed |
| Changes since last check | IDs and timestamps |
| Hypotheses | Open questions |
| Actions | Owner and due time |
| Next check | Date and reason |

Do not overwrite the prior checkpoint. A monitoring history should preserve the sequence of decisions.

