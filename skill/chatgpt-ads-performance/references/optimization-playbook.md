# Optimization playbook

## Contents

1. Optimization principles
2. Baseline record
3. Lever order
4. Decision matrix
5. Bid and budget changes
6. Context hints
7. Creative testing
8. Targeting and segments
9. Experiments
10. Rollback and verification

## 1. Optimization principles

Optimize the binding constraint, not the most visible metric.

Prefer:

- reversible before irreversible
- measurement fixes before media changes
- one causal change before bundles
- economic outcomes before CTR
- explicit hypotheses before experimentation
- completed attribution windows before judgment

Never use optimization as a synonym for "change something."

## 2. Baseline record

Before each change, record:

- timestamp and account timezone
- account and object IDs
- current configuration
- current and prior-period KPIs
- attribution settings
- target CPA, CAC, or ROAS
- evidence label
- diagnosis and alternative explanations
- proposed change
- expected direction and magnitude, if estimable
- earliest valid review date
- rollback condition

If the configuration cannot be reconstructed later, do not change it.

## 3. Lever order

Use this default order:

1. account, payment, policy, review, or serving repair
2. landing and conversion measurement repair
3. pause a clearly harmful entity
4. bid constraint or strategy
5. context hints and intent structure
6. creative argument and asset
7. platform, geography, product, or audience selection
8. budget

Budget is last because more budget amplifies the current system, including its defects.

## 4. Decision matrix

| Situation | Preferred action | Avoid |
|---|---|---|
| No impressions, approved and active | Check bid, hints, targeting, dates | Increasing budget first |
| Impressions, low CTR | Test creative argument or separate intent | Changing bid and creative together |
| Healthy CTR, low CVR | Audit tracking and landing | Declaring the ad successful |
| Healthy CPA, budget-limited | Controlled budget increase | Large one-step scale |
| Healthy CPA, delivery-limited | Bid/hint expansion test | Broad uncontrolled targeting |
| Poor CPA, insufficient data | Hold or gather more data | Pausing as a "winner/loser" call |
| Poor CPA, decision-ready | Pause or isolate cause | Averaging it with strong entities |
| Strong platform segment | Validate conversion quality | Narrowing based on clicks only |
| Tracking outage | Repair and annotate period | Optimizing from false zero conversions |

## 5. Bid and budget changes

### Fixed bid

Raise a fixed bid when:

- the ad group is eligible and approved
- targeting is not accidentally narrow
- bid_too_low or delivery history suggests auction constraint
- economics allow the higher ceiling

Lower a bid when:

- delivery is sufficient
- CPC or CPA is materially above target
- conversion quality is stable

Default step: 10–20%. Use smaller steps for high spend. Do not change again until at least 48–72 hours or one complete attribution cycle, unless a safety issue exists.

### Maximize Results

Use only when the current API and account support it, the campaign has a daily budget, the objective matches the strategy, and conversion tracking is healthy for conversion optimization.

Do not compare fixed and automated bidding in the same ad group. Record the strategy switch as a structural experiment.

### Budget scaling

Scale only when:

- tracking is healthy
- campaign meets the target with decision-ready evidence
- delivery is budget-constrained
- downstream capacity exists

Default increase: 10–20% per review cycle. Do not recommend a larger first step merely because the campaign spends its full budget. A larger step requires explicit user acceptance of additional volatility plus decision-ready economics, verified tracking, clear budget constraint, and downstream capacity. For low-volume campaigns, wait for a complete business cycle. Set a rollback trigger such as CPA above target by 20–30% over a decision-ready window.

Do not scale solely because daily budget was fully spent.

### Budget reduction

Reduce or pause when:

- economics are materially below target with sufficient evidence
- spend is pacing above the approved plan
- conversion quality deteriorates
- tracking or landing is broken and continued spend is unsafe

## 6. Context hints

Keep one product category or intent per ad group.

Use four registers:

- P: product and beneficiary description
- S: user situation or need
- C: likely conversation or question
- K: short topic or keyword control

For first campaigns, test P, C, and K with identical ads and distinct UTM content. Keep a K control unless data proves another structure superior.

When optimizing:

- compare styles at ad-group level
- preserve the winning control while testing challengers
- replace incoherent or redundant hints
- mine language from Search Console, paid-search terms, FAQs, support, sales calls, and landing pages
- do not claim that a hint is an exact-match keyword

No prompt-level trigger report exists. Optimize by outcome data.

## 7. Creative testing

Test arguments, not synonyms:

- price or economic value
- speed or convenience
- risk reduction
- outcome
- expertise or proof
- implementation simplicity

Keep the landing page and context hints constant for a creative test.

For multiple-image ads, use 4–6 distinct square images only if the account and current API support the format. The images share the copy and destination, so the test isolates the visual sequence, not the message.

Avoid:

- tiny text inside images
- logo-only images
- several creative changes inside one variant
- judging on CTR when conversion quality differs

Creative fatigue cannot be proven without reach and frequency. Use declining CTR with stable targeting as a hypothesis, not a fact.

## 8. Targeting and segments

Narrow a platform, geography, product, or audience only when:

- the segment has adequate volume
- conversion quality supports the difference
- the API allows the action
- the exclusion will not destroy learning volume

If conversion segmentation is unavailable, use external analytics joined by UTMs. Do not optimize from delivery metrics alone when the business outcome may differ.

Custom audiences require first-party rights and may be unavailable for EEA/Switzerland targeting.

## 9. Experiments

Every experiment needs:

- single primary hypothesis
- primary metric and guardrail metrics
- control and challenger
- isolated causal difference
- minimum sample or time window
- attribution settings
- success threshold
- stop-loss threshold
- decision date

Use sequential decisions:

1. safety stop
2. futility stop
3. winner declaration
4. continue collecting data

Do not peek daily and repeatedly declare a winner without accounting for the increased false-positive risk.

## 10. Rollback and verification

After an approved write:

1. verify the detail endpoint, not only a list
2. allow for short consistency lag
3. do not repeat the write because a stale read still shows the old value
4. confirm serving and review state
5. annotate the change timestamp
6. wait for the defined review window
7. compare against the saved baseline

Rollback actions should be prepared before the change:

- restore prior bid
- restore prior context hints
- restore prior platforms
- restore prior budget
- pause the new creative

Creative edits can trigger re-review; rolling back creative may also trigger review.
