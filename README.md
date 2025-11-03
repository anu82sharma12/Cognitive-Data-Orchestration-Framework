# Cognitive Data Orchestration Pipeline  
**Airflow + pandas • GitHub-Ready • 50 % Faster ETL**

**Before:** 4 hours manual CSV → clean → load  
**After:** 1.9 hours fully automated → **52 % time saved**

One-click DAG turns **10 raw CSVs** into **analytics-ready Parquet tables** with:
- Schema enforcement
- Smart deduplication
- Date parsing
- Incremental loads
- Slack alerts

Deploy in **5 minutes** on local Airflow or **free Astronomer Cloud**.

---

┌──────────────┐
│    start     │
└───────┬──────┘
        ▼
┌──────────────┐     ┌─────────────────┐
│ extract_csvs ├────►│ validate_schema │
└───────┬──────┘     └───────┬─────────┘
        ▼                    ▼
┌──────────────┐     ┌─────────────────┐
│ transform    ├────►│ dedupe_incr     │
└───────┬──────┘     └───────┬─────────┘
        ▼                    ▼
┌──────────────┐     ┌─────────────────┐
│ load_parquet ├────►│ notify_slack    │
└───────┬──────┘     └───────┬─────────┘
        ▼                    ▼
┌──────────────┐
│     end      │
└──────────────┘

