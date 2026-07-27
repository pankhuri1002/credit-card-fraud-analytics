# Credit Card Fraud Analytics

## Live dashboard

[**Open the interactive fraud analytics dashboard →**](https://pankhuri1002.github.io/credit-card-fraud-analytics/)

Recruiters can explore category risk, switch between fraud rate and case volume, adjust the minimum transaction threshold for state-level analysis, and compare fraudulent and legitimate transactions across transaction-amount bands.

## Executive summary

This portfolio project turns one month of historical card transactions into a decision-oriented fraud risk dashboard for compliance teams. It demonstrates business analysis, data-quality assessment, KPI design, Tableau dashboard development, dashboard storytelling, and evidence-based recommendations.

**Headline:** 180 of 42,308 transactions were labelled fraudulent (0.425%), representing $97,540.81 or 3.29% of transaction value. Fraud is concentrated in online shopping and other card-not-present categories, while transactions from midnight to 05:59 show a 0.821% fraud rate versus 0.327% during the rest of the day.

## Recruiter review path (5 minutes)

1. Open the [live interactive dashboard](https://pankhuri1002.github.io/credit-card-fraud-analytics/) for the business story and interactive views.
2. Read `docs/BRD.md` for scope, stakeholders, requirements, and acceptance criteria.
3. Review `docs/DATA_QUALITY.md` for the important data-quality findings and limitations.

## Business problem

AnalytIQ Edge needs to identify unusual spending patterns, segment fraud risk, and help compliance teams prioritize monitoring interventions. The project is historical and analytical; it does not build a real-time fraud model or claim that any demographic/job group causes fraud.

## Key findings

- **Category concentration:** `shopping_net` had 42 frauds and the highest category fraud rate (1.299%); together with `grocery_pos`, `shopping_pos`, and `misc_net`, it accounts for most labelled fraud.
- **Value exposure:** fraud represented 3.29% of transaction value despite only 0.425% of transactions, showing that count-only monitoring understates exposure.
- **Time risk:** midnight–05:59 had about 2.5× the fraud rate of other hours (0.821% vs 0.327%).
- **Amount risk:** 90 of 504 transactions of $500 or more were fraudulent (17.86%), while 43 of 747 transactions from $250 to $499 were fraudulent (5.76%).
- **Geography:** several states show elevated rates, but low-volume states need minimum-volume controls and follow-up validation.

## Recommended actions

1. Strengthen card-not-present monitoring by prioritizing online shopping transactions, especially overnight.
2. Apply additional verification to unusually high-value transactions, especially those of $250 or more.
3. Combine amount deviation, category, merchant history, and the customer’s normal spending pattern instead of relying on one warning sign.
4. Require minimum sample sizes before escalating geographic or other customer segments.
5. Treat the findings as initial risk indicators. Because the analysis covers one month, use these patterns to select transactions for additional verification—not automatic blocking.

## Tools and methods

Tableau for KPI calculations, data visualisation and interactive dashboard development; CSV files as the project data source; BA documentation for requirements traceability.

## Data scope and limitations

- 42,308 transactions from 1–31 December 2019; 180 labelled frauds.
- The data is historical and anonymized; findings are not a production fraud model.
- `location_data.csv` stores card numbers in scientific notation, producing only ~39.95% reliable join coverage. Dashboard geography therefore uses coordinates already present in the transaction table.
- Sensitive fields such as card number, name, street, and date of birth are excluded from portfolio outputs.
