# Credit Card Fraud Analytics

## Live dashboard

[**Open the interactive fraud analytics dashboard →**](https://pankhuri1002.github.io/credit-card-fraud-analytics/?v=20260727-dashboard-v2)

Recruiters can explore category risk, inspect the fraud rate for every transaction hour, apply volume safeguards to state comparisons, compare fraud rates across transaction-amount bands, and use the merchant risk matrix to prioritize merchant review.

## Executive summary

This portfolio project turns one month of historical card transactions into a decision-oriented fraud risk dashboard for compliance teams. It demonstrates business analysis, data-quality assessment, KPI design, interactive dashboard development, dashboard storytelling, and evidence-based recommendations.

**Headline:** 180 of 42,308 transactions were labelled fraudulent (0.425%), representing $97,540.81 or 3.29% of transaction value. Fraud is concentrated in online shopping and other card-not-present categories. The 22:00–03:59 late-night window recorded 163 frauds among 9,999 transactions—a 1.630% fraud rate—with the highest individual hourly rates at 22:00 and 23:00.

## Recruiter review path (5 minutes)

1. Open the [live interactive dashboard](https://pankhuri1002.github.io/credit-card-fraud-analytics/?v=20260727-dashboard-v2) for the business story and interactive views.
2. Read `docs/BRD.md` for scope, stakeholders, requirements, and acceptance criteria.
3. Review `docs/DATA_QUALITY.md` for the important data-quality findings and limitations.

## Business problem

AnalytIQ Edge needs to identify unusual spending patterns, segment fraud risk, and help compliance teams prioritize monitoring interventions. The project is historical and analytical; it does not build a real-time fraud model or claim that any demographic/job group causes fraud.

## Key findings

- **Category concentration:** `shopping_net` had 42 frauds and the highest category fraud rate (1.299%); together with `grocery_pos`, `shopping_pos`, and `misc_net`, it accounts for most labelled fraud.
- **Value exposure:** fraud represented 3.29% of transaction value despite only 0.425% of transactions, showing that count-only monitoring understates exposure.
- **Time risk:** the highest individual hourly rates occurred at 23:00 (2.212%) and 22:00 (2.140%). Across 22:00–03:59, 163 of 9,999 transactions were labelled fraudulent (1.630%).
- **Amount risk:** the within-band fraud rate was 17.86% for $500+ transactions (90 ÷ 504) and 5.76% for $250–$499 transactions (43 ÷ 747); every band below $250 remained under 0.26%.
- **Geography:** the dashboard now tests every state against the selected minimum volume before displaying the ten highest rates. At a 100-transaction minimum, Nevada, Tennessee and West Virginia have the highest observed rates; low-volume results still require follow-up validation.
- **Merchant risk:** 516 merchants had at least 50 transactions. The matrix identifies 96 merchants above both the median merchant volume of 62 transactions and the overall 0.425% fraud rate; these are review priorities, not evidence that a merchant caused fraud.

## Recommended actions

1. Prioritize activity from 22:00–03:59 for additional verification, especially at 22:00 and 23:00 where the highest hourly fraud rates were observed.
2. Prioritize transactions of $250 or more for additional verification when other warning signs are present; do not block them based on amount alone.
3. Review merchants in the matrix’s top-right quadrant first, then inspect their category, time and amount patterns before escalating.
4. Apply the selected minimum transaction count to all states before ranking them, and validate low-volume state patterns before escalating monitoring.
5. Combine amount, category, time, merchant and geography rather than relying on one warning sign. Because the analysis covers one month, use these patterns for additional verification—not automatic blocking.

## Tools and methods

CSV source data, calculated fraud-risk KPIs, an interactive web dashboard, and BA documentation for requirements traceability.

## Data scope and limitations

- 42,308 transactions from 1–31 December 2019; 180 labelled frauds.
- The data is historical and anonymized; findings are not a production fraud model.
- `location_data.csv` stores card numbers in scientific notation, producing only ~39.95% reliable join coverage. Dashboard geography therefore uses coordinates already present in the transaction table.
- Sensitive fields such as card number, name, street and date of birth are excluded from the dashboard and narrative outputs. The original public learning dataset remains in `data/raw/` for source traceability.
