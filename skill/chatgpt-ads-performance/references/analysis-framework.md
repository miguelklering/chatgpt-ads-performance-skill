# Performance analysis framework

## Contents

1. Analysis order
2. Data contract
3. KPI definitions
4. Profitability model
5. Period comparison
6. Evidence and statistical discipline
7. Diagnostic tree
8. Entity classification
9. Segmentation
10. Forecasting
11. Common analytical errors

## 1. Analysis order

Analyze in this order:

1. account eligibility and campaign serving
2. data integrity and attribution
3. budget delivery and pacing
4. impressions and auction access
5. clicks and creative response
6. conversions and landing response
7. unit economics
8. scale capacity

Stop downstream conclusions when an upstream layer is invalid. For example, broken conversion tracking invalidates CPA, CVR, ROAS, and conversion-based optimization.

## 2. Data contract

Record these parameters with every analysis:

- account, currency, and timezone
- exact start and end date
- whether the end date is inclusive or exclusive
- current and comparison periods
- entity level and filters
- click attribution window
- view attribution window
- attribution time basis: ad event or conversion event
- conversion event and source
- data extraction time
- whether current-day data is included

Use periods ending yesterday unless the task is incident monitoring. Current impressions and clicks may arrive before finalized spend; conversions may arrive later. Prefer API-returned CPC and CPM for very recent windows.

Never compare reports with different attribution settings without labeling the difference.

## 3. KPI definitions

Use decimal ratios internally and percentages for display.

| KPI | Formula | Interpretation |
|---|---|---|
| CTR | clicks / impressions | Creative and contextual response |
| CPC | spend / clicks | Cost of traffic |
| CPM | spend × 1,000 / impressions | Cost of delivery |
| CVR | conversions / clicks | Post-click and conversion response |
| CPA | spend / conversions | Cost per attributed conversion |
| Revenue per click | revenue / clicks | Economic value of traffic |
| ROAS | revenue / spend | Gross revenue efficiency |
| Contribution ROAS | contribution profit before ads / spend | Margin-aware efficiency |
| Profit after ads | contribution profit before ads − spend | Absolute return |
| Budget delivery | spend / planned spend | Pacing |
| Impression share | unavailable unless the API supplies it | Do not infer |

Handle zero denominators as unavailable, not zero.

For leads, distinguish:

- platform lead
- marketing-qualified lead
- sales-qualified lead
- opportunity
- won customer

Calculate cost per stage only when CRM data exists. Do not equate a form event with customer acquisition.

## 4. Profitability model

Request business targets before economic recommendations:

- target CPA or CAC
- target ROAS
- average order value
- gross or contribution margin
- lead-to-sale rate
- average first-sale contribution
- lifetime value when reliably known
- refund, cancellation, or churn assumptions

Useful formulas:

- E-commerce break-even CPA = average order value × contribution margin rate
- Lead-gen break-even CPL = contribution per won customer × lead-to-sale rate
- Break-even CVR = CPC / break-even CPA
- Maximum CPC at target CPA = target CPA × expected CVR
- Required conversions = planned spend / target CPA
- Required clicks = required conversions / expected CVR
- Required impressions = required clicks / expected CTR

Use contribution margin rather than revenue when possible. ROAS can look healthy while profit is negative.

If targets are absent:

- report operational efficiency
- show scenario ranges instead of one answer
- mark profitability as not assessable
- never invent an industry benchmark

## 5. Period comparison

Use the same number of complete days and the same weekday mix. For low-volume accounts, compare 28 days with the prior 28 days rather than 7 days.

Decompose changes:

- Spend = volume × unit cost
- Clicks = impressions × CTR
- Conversions = clicks × CVR
- CPA = CPC / CVR
- Revenue = conversions × value per conversion

When CPA worsens, state whether it is mainly:

- CPC inflation
- CVR decline
- both
- mix shift between entities or segments
- delayed conversion attribution

Separate absolute change from percentage change. Large percentages from tiny bases are not material by themselves.

## 6. Evidence and statistical discipline

Use these default evidence labels unless the business supplies better thresholds:

- insufficient: fewer than 30 clicks for a rate decision, or fewer than 3 conversions for a CPA decision
- directional: 30–99 clicks or 3–9 conversions
- decision-ready: at least 100 clicks and at least 10 conversions, with a complete attribution window

These are safeguards, not universal statistical guarantees.

For variant comparisons:

- compare identical date ranges and attribution settings
- isolate one causal difference when possible
- use at least a full business cycle
- report conversion-rate confidence intervals
- avoid declaring a winner when intervals strongly overlap
- account for multiple comparisons when testing many variants

Use a two-proportion test only when clicks and conversions are available for both variants. Statistical significance does not guarantee economic significance.

Override sample thresholds for:

- policy violations
- broken links
- overspend
- duplicate conversion events
- targeting the wrong country
- account or payment incidents

Those require immediate action.

## 7. Diagnostic tree

### No or near-zero impressions

Check:

1. account, campaign, group, and ad status
2. review approval and serving issues
3. campaign dates and budget
4. spend limit or payment issue
5. targeting size and accidental exclusions
6. landing eligibility
7. bid_too_low and effective bid
8. context hints that are too narrow or incoherent

Do not increase budget before confirming the campaign can enter auctions.

### Impressions but weak CTR

Possible causes:

- weak or generic creative
- offer not relevant to the conversation
- mixed intent inside one ad group
- context hints too broad
- image unreadable at small size
- message and landing mismatch

Test a distinct argument, not a paraphrase. Keep the targeting constant when testing creative.

### Clicks but weak CVR

Check:

- conversion tracking and event linkage
- landing speed, mobile rendering, redirects, and preserved oppref
- offer continuity between ad and page
- price, friction, trust, and form quality
- geography and platform segments
- lead quality downstream in CRM

Do not blame context hints until tracking and landing are verified.

### Good CPA but little volume

Check:

- budget constraint
- bid constraint
- narrow hints or targeting
- limited approved creative
- eligible user population

Scale one dimension at a time. Protect CPA with a rollback threshold.

### High spend and no conversions

First determine whether conversions are truly absent or not being recorded. If tracking is healthy, compare spend with target CPA:

- below 1× target CPA: usually insufficient evidence
- 1–2× target CPA: watch and diagnose
- above 2× target CPA with adequate clicks: candidate for pause or material change

These are default guardrails, not automatic actions.

### Healthy platform metrics but poor business result

Check:

- conversion event is too shallow
- lead-to-sale rate
- average order value or customer quality
- refunds, churn, or margin
- attribution over-credit

Optimize to the deepest reliable event, not the easiest event.

## 8. Entity classification

Classify using targets and evidence:

- healthy: meets economic target with decision-ready evidence
- watch: near target or evidence still directional
- constrained: economics are healthy but delivery is limited
- inefficient: materially misses target with decision-ready evidence
- tracking-risk: media data exists but conversion measurement is invalid
- insufficient-data: no safe performance conclusion

Never call an entity inefficient solely because it spent less than another entity.

## 9. Segmentation

Inspect country, device, product, and platform only when:

- the segment has enough volume
- the segment can be acted on
- conversion reporting is available or business analytics can join it

Beware Simpson's paradox: total performance can move because spend shifted toward a different segment. Report mix effects.

There is no prompt or search-term report. Do not claim to know which private user conversations triggered an ad.

## 10. Forecasting

Build three scenarios:

- conservative
- base
- upside

Use observed CTR, CPC, CVR, and value ranges. Show formulas and assumptions. Cap the forecast by:

- eligible audience and delivery history
- daily budget
- sales or fulfillment capacity
- measurement uncertainty

Do not project linearly beyond two to three times observed spend without warning that marginal efficiency may decline.

## 11. Common analytical errors

Avoid:

- using the current incomplete day in a period comparison
- mixing click-through and total conversions
- recomputing recent CPC from non-finalized fields when API CPC exists
- comparing different attribution windows
- treating view-through conversion as click-based bidding evidence
- using CTR as the main success metric
- declaring a winner from tiny samples
- optimizing several levers at once
- scaling before verifying conversion tracking
- confusing CPA with CAC
- ignoring margin and sales quality

