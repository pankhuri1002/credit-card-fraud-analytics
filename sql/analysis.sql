-- PostgreSQL portfolio queries. Card numbers must be loaded as TEXT.
CREATE SCHEMA IF NOT EXISTS finance;
SET search_path TO finance;

-- Headline KPIs
SELECT COUNT(*) AS transactions,
       SUM(is_fraud) AS frauds,
       ROUND(100.0 * SUM(is_fraud) / COUNT(*), 3) AS fraud_rate_pct,
       ROUND(SUM(amt)::numeric, 2) AS transaction_amount,
       ROUND(SUM(amt) FILTER (WHERE is_fraud=1)::numeric, 2) AS fraud_amount
FROM cc_data;

-- Category risk: show volume and rate together
SELECT category, COUNT(*) AS transactions, SUM(is_fraud) AS frauds,
       ROUND(100.0*SUM(is_fraud)/COUNT(*),3) AS fraud_rate_pct,
       ROUND(AVG(amt)::numeric,2) AS avg_amount
FROM cc_data GROUP BY category ORDER BY fraud_rate_pct DESC;

-- Overnight comparison
SELECT CASE WHEN EXTRACT(HOUR FROM trans_date_trans_time) BETWEEN 0 AND 5
            THEN '00:00-05:59' ELSE '06:00-23:59' END AS time_band,
       COUNT(*) transactions, SUM(is_fraud) frauds,
       ROUND(100.0*SUM(is_fraud)/COUNT(*),3) fraud_rate_pct
FROM cc_data GROUP BY 1 ORDER BY fraud_rate_pct DESC;

-- Top merchants
SELECT merchant, COUNT(*) transactions FROM cc_data GROUP BY merchant ORDER BY transactions DESC LIMIT 10;

-- Requested aggregations
SELECT gender, ROUND(AVG(amt)::numeric,2) avg_amount FROM cc_data GROUP BY gender;
SELECT category, COUNT(*) transactions FROM cc_data GROUP BY category ORDER BY transactions DESC;
SELECT TRIM(TO_CHAR(trans_date_trans_time,'Day')) weekday, ROUND(AVG(amt)::numeric,2) avg_amount
FROM cc_data GROUP BY 1 ORDER BY avg_amount DESC;

-- Location join QA: never use a low-coverage join silently
SELECT COUNT(*) transaction_rows,
       COUNT(l.cc_num) matched_rows,
       ROUND(100.0*COUNT(l.cc_num)/COUNT(*),2) join_coverage_pct
FROM cc_data c LEFT JOIN location_data l ON c.cc_num::text=l.cc_num::text;
