# Data Quality Assessment

**Assessment:** Share with caveats for historical descriptive analysis.

| Check | Result | Impact |
|---|---:|---|
| Transaction rows | 42,308 | Expected transaction grain |
| Unique transaction IDs | 42,308 | No duplicate IDs |
| Exact duplicate rows | 0 | No duplication detected |
| Missing values | 0 | Complete supplied transaction fields |
| Non-positive amounts | 0 | No invalid amount values |
| Coordinate validity | 100% | Coordinates fall in valid latitude/longitude ranges |
| Location reference join coverage | 39.95% | Material blocker for a production dimension join |

## Material issue

`location_data.csv` represents card numbers in scientific notation. This loses exact digits for long identifiers and prevents a dependable card-level join. The dashboard uses the latitude and longitude already present in `cc_data_dec19.csv`. A production solution should ingest the key as text from the source and enforce uniqueness and referential-integrity tests.

## Privacy controls

Portfolio outputs exclude card number, customer name, street address, date of birth, and full transaction-level customer detail. Demographic and job results are aggregate, descriptive signals only and must not be used as standalone decision rules.
