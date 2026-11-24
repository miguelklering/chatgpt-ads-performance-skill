# Policy and operational safety

## Contents

1. Source of truth
2. Hard stops
3. Creative preflight
4. Landing preflight
5. Audience and privacy
6. Spend and account safety
7. Change safety

## 1. Source of truth

Read the current official OpenAI Ad Policies and Ad Tools Terms before creating or editing creative. Policies change faster than bundled skills. If this file conflicts with official policy, official policy wins.

## 2. Hard stops

Stop and explain when:

- the product category is prohibited in the target market
- the advertiser lacks required eligibility or licensing
- copy or landing makes deceptive or unsupported claims
- the landing is unavailable, gated, deceptive, or unrelated
- the wrong legal entity, account, currency, or country is selected
- spend protection is absent and the user has not accepted a safe fallback
- audience data rights are unclear
- the requested action would circumvent review or enforcement

Do not rewrite prohibited advertising merely to evade review.

## 3. Creative preflight

Check:

- title and body length against the current API
- professional, truthful language
- no guarantee, false scarcity, fabricated endorsement, or unsupported ranking
- no implication of OpenAI or ChatGPT endorsement
- image ownership or license
- image and copy consistency
- landing continuity
- market-specific category restrictions
- no sensitive personal inference

Lint success is not policy approval.

## 4. Landing preflight

Run landing-check and verify:

- HTTPS public URL
- 200 response for browser and OAI-AdsBot
- robots allow the required crawler
- no captcha or JS challenge
- favicon present
- redirects preserve oppref and UTMs
- content matches the advertiser and offer
- mobile rendering works
- no prohibited downstream content
- privacy and consent controls are appropriate

## 5. Audience and privacy

Use only first-party data the advertiser has rights to use. Never use brokered or scraped lists.

Confirm:

- legal basis and consent
- correct hashing and normalization
- secure server-side handling
- audience market eligibility
- EEA/Switzerland limitations
- no secrets or raw identifiers in committed files

## 6. Spend and account safety

Before the first write:

- check spend-limits
- confirm account currency and timezone
- confirm campaign budget and end date
- warn that daily delivery may exceed a nominal daily target when platform rules allow
- define maximum test loss

If account-level limits are unavailable, use a user-approved daily campaign budget, end date, and frequent monitoring.

Never broaden market, raise budget, or activate without explicit approval.

## 7. Change safety

For every write:

1. capture current detail
2. produce dry-run or request diff
3. state risk and rollback
4. obtain approval
5. execute one confirmed operation
6. verify detail
7. annotate change time

Never use force unless requested by name and the consequence is explained.

Pause is reversible. Archive is not.

One-time secrets belong in a secret manager or environment variable, never in chat, reports, or version control.
