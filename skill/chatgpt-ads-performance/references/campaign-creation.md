# Campaign creation playbook

## Contents

1. Required brief
2. Readiness gates
3. Architecture
4. Context-hint design
5. Creative design
6. Measurement and attribution
7. Plan, dry-run, and activation
8. Post-launch learning plan

## 1. Required brief

Gather:

- business and offer
- landing URL
- target geography and language
- primary conversion and its business value
- target CPA, CAC, or ROAS
- average order value and margin when available
- sales or fulfillment capacity
- daily budget and maximum test loss
- campaign dates
- platform restrictions
- available images and brand rules
- policy-sensitive category or claims
- Pixel/CAPI and analytics status

Ask only for missing information that materially changes the setup. Mark assumptions.

## 2. Readiness gates

Do not create while a critical gate is red:

1. correct ad account, legal entity, currency, and timezone
2. approved brand and working payment method
3. spend fuse or explicit campaign-level fallback
4. allowed category and compliant claims
5. public landing page returning 200 to OAI-AdsBot
6. robots, WAF, redirects, favicon, and oppref pass
7. conversion event deployed and linked
8. assets licensed and usable
9. current API support validated

If the user explicitly accepts a noncritical gap, record it and its consequence. Never waive a policy, wrong-account, or unsafe-spend problem.

## 3. Architecture

Use:

- campaign for objective, budget, dates, market, platform, audiences, and conversion linkage
- ad group for one intent, context-hint strategy, bid, and product set
- ad for one message and visual treatment

Start new advertisers on clicks with a daily budget when conversion history is not reliable. Use conversion optimization only with a supported standard event and healthy history. Objective choices may be immutable.

Keep one market and one objective per campaign when economics or targeting differ materially.

Recommended initial shape:

- one campaign
- three to six ad groups
- one intent per ad group
- three to five distinct creative arguments per group when budget supports learning
- a control group for context-hint style

Do not fragment a small budget across too many entities.

## 4. Context-hint design

Use:

- P: product, beneficiary, and use case
- S: situation or need
- C: conversation or question
- K: short topic or keyword control

For a first test, create P, C, and K groups using identical ads and separate UTM content values. Add S only when budget can support another cell.

Mine language from:

- Search Console
- paid-search terms
- customer FAQs
- support and sales conversations
- on-site search
- landing-page headings

Hints are relevance signals, not exact-match keywords. Do not imply access to user chats.

## 5. Creative design

Write for the small placement:

- concrete benefit
- one claim
- no unsupported superlative
- continuity with the landing page
- distinct argument per variant

Use the current API limits from official docs. At the 2026-10-26 API update, enabled accounts may use four to six distinct square images through creative.file_ids. The images share title, body, and destination. Feature-detect because availability is account-gated.

For one image:

- use a recognizable product or scene
- ensure square crop works
- avoid logo-only artwork
- avoid small embedded text

For multiple images:

- use four to six square assets
- define a visual sequence
- do not mix unrelated products
- validate that the CLI and account support the format
- do not send both singular and plural image fields

## 6. Measurement and attribution

Before launch:

- create or confirm Pixel/CAPI source
- create the standard event setting
- link the event to every campaign, including CPC campaigns
- deduplicate browser and server events with the same event ID
- preserve and pass oppref
- configure consent and CSP
- add UTMs at a consistent level

Record explicit click attribution, view attribution, and time basis for reporting. The API added selectable attribution settings to Insights on 2026-09-30; omitted values can change totals compared with older reports.

Use a full UTM template on each ad group when that is the live-verified operating pattern. Keep utm_content unique for each experimental cell.

## 7. Plan, dry-run, and activation

Prefer a single plan file:

- paused campaign
- daily budget
- end date
- correct locations and platforms
- conversion event linkage
- ad-group bids and context hints
- UTM templates
- ads and image assets

Run:

    plan-apply --file plan.json

Show the dry-run, warnings, counts, expected duration, and policy findings. Pause for approval.

Then, only with approval:

    plan-apply --file plan.json --confirm

Use idempotency state for resume. A repeated run should report differences; do not sync them without another dry-run and approval.

Verify through detail endpoints, review, preview, landing check, and conversion check. Allow for short consistency lag and do not repeat a write because a read is stale.

Activate only after approval and review success:

1. ads
2. ad groups
3. campaign

## 8. Post-launch learning plan

Define before activation:

- primary metric
- guardrail metrics
- target
- maximum test loss
- earliest review date
- minimum sample
- stop-loss rule
- winner rule
- next creative or hint hypothesis

The campaign is not complete until its monitoring and decision plan exists.

