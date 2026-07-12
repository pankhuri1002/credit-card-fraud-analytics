import json
from pathlib import Path
import pandas as pd
import numpy as np

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "portfolio" / "data" / "processed"
OUT.mkdir(parents=True, exist_ok=True)

tx = pd.read_csv(ROOT / "upload" / "cc_data_dec19.csv", low_memory=False)
loc = pd.read_csv(ROOT / "upload" / "location_data.csv")
tx.columns = tx.columns.str.replace("\ufeff", "", regex=False)
tx["trans_date_trans_time"] = pd.to_datetime(tx["trans_date_trans_time"], dayfirst=True)
tx["dob"] = pd.to_datetime(tx["dob"], dayfirst=True)
tx["cc_key"] = pd.to_numeric(tx["cc_num"], errors="coerce").round().astype("Int64").astype(str)
loc["cc_key"] = pd.to_numeric(loc["cc_num"], errors="coerce").round().astype("Int64").astype(str)
tx["age"] = ((tx["trans_date_trans_time"] - tx["dob"]).dt.days / 365.25).astype(int)
tx["age_band"] = pd.cut(tx["age"], [0, 29, 39, 49, 59, 69, 200], labels=["Under 30","30-39","40-49","50-59","60-69","70+"])
tx["hour"] = tx["trans_date_trans_time"].dt.hour
tx["day_name"] = tx["trans_date_trans_time"].dt.day_name()
tx["risk_period"] = np.where(tx["hour"].between(0,5), "00:00-05:59", "06:00-23:59")

def risk_table(df, group, min_tx=1):
    g = df.groupby(group, observed=True).agg(transactions=("trans_num","size"), frauds=("is_fraud","sum"), amount=("amt","sum"), fraud_amount=("amt",lambda s: s[df.loc[s.index,"is_fraud"].eq(1)].sum()), avg_amount=("amt","mean")).reset_index()
    g["fraud_rate_pct"] = 100*g["frauds"]/g["transactions"]
    return g[g.transactions >= min_tx].sort_values(["fraud_rate_pct","frauds"], ascending=False)

profile = {
    "rows": len(tx), "columns": len(tx.columns), "date_min": str(tx.trans_date_trans_time.min()), "date_max": str(tx.trans_date_trans_time.max()),
    "unique_transactions": int(tx.trans_num.nunique()), "duplicate_transaction_ids": int(tx.trans_num.duplicated().sum()),
    "exact_duplicate_rows": int(tx.duplicated().sum()), "frauds": int(tx.is_fraud.sum()), "fraud_rate_pct": float(100*tx.is_fraud.mean()),
    "total_amount": float(tx.amt.sum()), "fraud_amount": float(tx.loc[tx.is_fraud.eq(1),"amt"].sum()),
    "unique_cards": int(tx.cc_key.nunique()), "location_rows": len(loc), "location_unique_cards": int(loc.cc_key.nunique()),
    "join_coverage_pct": float(100*tx.cc_key.isin(set(loc.cc_key)).mean()),
    "missing_by_column": {k:int(v) for k,v in tx.isna().sum().items() if v},
    "invalid_amount_count": int((tx.amt <= 0).sum()), "invalid_lat_count": int((~tx.lat.between(-90,90)).sum()), "invalid_long_count": int((~tx.long.between(-180,180)).sum())
}
(OUT / "profile.json").write_text(json.dumps(profile, indent=2))

tables = {
    "category_risk": risk_table(tx, "category"),
    "gender_risk": risk_table(tx, "gender"),
    "age_risk": risk_table(tx, "age_band"),
    "state_risk": risk_table(tx, "state", min_tx=100),
    "hour_risk": risk_table(tx, "hour"),
    "risk_period": risk_table(tx, "risk_period"),
    "job_risk": risk_table(tx, "job", min_tx=100),
    "merchant_risk": risk_table(tx, "merchant", min_tx=50),
}
for name, df in tables.items(): df.to_csv(OUT / f"{name}.csv", index=False)

fraud = tx[tx.is_fraud.eq(1)].copy()
fraud[["trans_num","trans_date_trans_time","category","amt","gender","state","age_band","job","merchant","lat","long"]].sort_values("amt",ascending=False).head(100).to_csv(OUT / "top_fraud_transactions.csv", index=False)
print(json.dumps(profile, indent=2))
for n in ["category_risk","gender_risk","age_risk","state_risk","risk_period","job_risk"]:
    print("\n",n); print(tables[n].head(15).to_string(index=False))
