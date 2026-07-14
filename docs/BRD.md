# Business Requirements Document

## 1. Project Header

| Field | Details |
|---|---|
| Project Name | Credit Card Fraud Risk Dashboard |
| Organization | AnalytIQ Edge |
| Project Manager | Jessica |
| Prepared By | Business Analyst |
| Document Status | Draft |
| Version | 1.0 |
| Date | 14 July 2026 |

## 2. Executive Summary

The project aims to analyse historical credit card transactions to identify unusual spending patterns and areas with higher fraud exposure. The findings will be presented through an interactive dashboard to support fraud monitoring, investigation prioritization and business decision-making.

## 3. Project Objectives

- Measure the overall number, rate and monetary value of fraudulent transactions.
- Identify transaction categories, merchants and locations with higher fraud exposure.
- Compare fraudulent and legitimate transactions to identify unusual spending patterns.
- Analyse how fraud varies by transaction time and relevant customer segments.
- Develop an interactive dashboard that presents key fraud indicators and findings.
- Provide actionable recommendations for improving fraud-monitoring strategies.

## 4. Project Scope

### In Scope

- Analysis of historical credit card transaction and location data.
- Data-quality assessment and validation.
- Fraud analysis by amount, category, merchant, time, location and customer segment.
- Development of fraud-related KPIs and an interactive dashboard.
- Documentation of findings, limitations and recommendations.

### Out of Scope

- Real-time fraud monitoring and alerts.
- Automatic approval, rejection or blocking of transactions.
- Development of a production fraud-prediction model.
- Integration with live banking systems or external APIs.
- Investigation of individual fraud cases.

## 5. Stakeholders

| Stakeholder | Responsibility |
|---|---|
| Project Manager | Approves the project scope, timeline and final deliverables. |
| Fraud Investigation Team | Reviews identified fraud patterns and prioritizes areas for investigation. |
| Compliance Team | Ensures that the analysis supports applicable monitoring policies and practices. |
| Risk Management Team | Assesses financial and operational exposure associated with fraud. |
| Business Analyst | Defines requirements, coordinates stakeholders and translates findings into business recommendations. |
| Data Analyst | Validates the data, performs the analysis and generates insights. |
| Dashboard Developer | Creates the interactive dashboard based on approved requirements. |
| Data Privacy and Security Team | Ensures that the data and analytical outputs are handled securely. |
| Senior Management | Reviews major findings and makes strategic fraud-monitoring decisions. |

## 6. Business Requirements

| ID | Business Requirement | Priority | Purpose |
|---|---|---|---|
| BR-01 | The solution must display total transactions, fraudulent transactions, fraud rate and fraud amount. | High | Provide an overall view of fraud exposure. |
| BR-02 | The solution must analyse fraud by transaction category. | High | Identify categories requiring stronger monitoring. |
| BR-03 | The solution must compare transaction amounts for fraudulent and legitimate transactions. | High | Detect unusual spending behaviour. |
| BR-04 | The solution must analyse fraud by merchant, time and geographical location. | High | Identify where and when fraud is concentrated. |
| BR-05 | The solution should analyse fraud across relevant customer segments. | Medium | Understand differences in observed fraud patterns. |
| BR-06 | The dashboard must provide relevant filters for interactive analysis. | High | Allow stakeholders to explore specific segments and risk areas. |
| BR-07 | The displayed metrics must reconcile with the validated source data. | High | Ensure that stakeholders can trust the results. |
| BR-08 | The solution must present key findings, limitations and recommended actions. | Medium | Support informed monitoring and investigation decisions. |

## 7. Constraints and Assumptions

### Constraints

- The analysis is limited to the period and fields available in the supplied datasets.
- The location file may have card-number formatting issues that affect join accuracy.
- Historical data cannot provide real-time fraud detection.
- Fraud patterns with small transaction volumes may not be reliable for decision-making.
- The dashboard will not have a live data connection.

### Assumptions

- The `is_fraud` field correctly identifies fraudulent and legitimate transactions.
- Transaction amounts and timestamps are recorded consistently.
- The transaction dataset is the primary source for calculating project metrics.
- Stakeholders will use the dashboard for monitoring and investigation support, not automatic transaction decisions.

## 8. Cost-Benefit Analysis

| Area | Cost/Effort | Expected Benefit |
|---|---|---|
| Data analysis | Time required to validate and analyse transaction data | Faster identification of fraud patterns and risk concentrations |
| Dashboard development | Time required to design, build and test the dashboard | Reduced manual reporting and easier access to fraud insights |
| Documentation | Time required to define requirements and record findings | Improved clarity, consistency and future maintainability |
| Monitoring recommendations | Stakeholder review and validation effort | Better prioritization of fraud-monitoring and investigation activities |

**Overall assessment:** The project requires limited development cost because it uses existing data and analytical tools. Its expected benefits include reduced manual analysis, clearer fraud visibility and better prioritization of monitoring efforts.
