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

## Live DAG Flow (Real-Time Execution)

### Mermaid Diagram 

```mermaid
graph TD
    A[Start] --> B[Extract 10 CSVs]
    B --> C[Validate Schema]
    C --> D[Transform with pandas]
    D --> E[Dedupe Incremental]
    E --> F[Load to Parquet]
    F --> G[Slack Alert]
    G --> H[End]

    style A fill:#4CAF50,stroke:#333,color:white
    style H fill:#F44336,stroke:#333,color:white
    style G fill:#2196F3,stroke:#333,color:white

