# Business Requirements Document

## Project header

| Field | Value |
|---|---|
| Project | Credit Card Fraud Risk Dashboard |
| Sponsor/Manager | Jessica |
| Analyst | Business Analyst |
| Status | Draft |
| Submission date | 12 July 2026 |

## Executive summary

Create a historical fraud analytics solution that identifies unusual spending patterns, segments fraud exposure, and gives compliance stakeholders a concise dashboard for prioritizing investigation and monitoring improvements.

## Objectives

1. Quantify labelled fraud count, rate, and monetary exposure for the supplied period.
2. Identify categories, time windows, locations, and customer segments with elevated observed fraud risk.
3. Deliver a dashboard whose headline metrics reconcile to the source data.
4. Provide reusable SQL and documented metric definitions for auditability.
5. Translate findings into targeted, non-discriminatory monitoring recommendations.

## Scope

**In scope:** historical profiling; data-quality checks; category, time, state, gender, age-band, job-role and merchant analysis; aggregate dashboard; SQL; requirements and recommendations.

**Out of scope:** real-time alerts; API integrations; predictive model deployment; automatic card blocking; causal claims; production identity resolution; personally identifiable detail in public outputs.

## Stakeholders

| Role | Responsibility |
|---|---|
| Jessica, Sponsor | Approves scope and outcomes |
| Compliance/Fraud Lead | Defines risk priorities and uses findings |
| Business Analyst | Requirements, analysis, dashboard, recommendations |
| Data Analyst/Engineer | Data extraction, joining, quality and reproducibility |
| Information Security/Privacy | Reviews handling of sensitive attributes |

## Business requirements

| ID | Requirement | Priority | Acceptance criterion |
|---|---|---|---|
| BR-01 | Reconcile total transactions and fraud labels | Must | Dashboard totals equal validated source totals |
| BR-02 | Show fraud count, rate, and value exposure | Must | All three metrics include definitions and denominators |
| BR-03 | Segment risk by category and time | Must | Viewer can compare volume and rate without conflating them |
| BR-04 | Support demographic/geographic exploration | Should | Aggregates include sample size and responsible-use caveat |
| BR-05 | Protect sensitive customer data | Must | No card numbers, names, addresses, or DOB in outputs |
| BR-06 | Document source quality and join coverage | Must | Location-key limitation is visible |
| BR-07 | Provide reproducible SQL | Should | Queries cover requested exploration and aggregation tasks |

## Constraints and assumptions

The dataset covers one historical month; fraud labels are treated as ground truth for descriptive analysis. Location reference keys are degraded by scientific notation. Amount is assumed to be USD based on the source dataset convention. No live refresh is included.

## Cost-benefit assessment

The solution uses existing data and lightweight tools, so implementation effort is primarily analyst time. Benefits include faster risk triage, repeatable reporting, clearer concentration analysis, and reduced manual spreadsheet review. Production benefits require validation against newer data and operational baselines.
