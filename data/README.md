# Data files

This project uses the original public files supplied with the capstone:

- `cc_data_dec19.csv` - transaction-level credit card data in its original structure
- `location_data.csv` - card-location reference data in its original structure

The repository intentionally keeps these files under `data/raw/` so recruiters can distinguish source data from analysis code and dashboard outputs.

## Important note

The fields resemble personal and payment information, but the project treats the dataset as public, anonymized/synthetic learning data. It must not be interpreted as current real customer information.

## Reproducibility

The dashboard metrics and SQL analysis are calculated from the original transaction-level fields. No pre-aggregated CSV files are required to understand or reproduce the project.
