## Task 3: Analytics Layer with dbt

### Overview  
Transform the telemetry table into analytics-ready models for Power BI dashboards.

### Problem Context  
Zippy’s Paris ops team needs insights like battery health trends and idle hotspots. dbt will help model these metrics from the raw telemetry.

### Tech Tools  
- dbt  
- PostgreSQL or DuckDB (for local dev)  
- SQL  
- GitHub  

### Email from Ravi Patel

> **From:** Ravi Patel  
> **Subject:** Time for dbt Models  
>  
> Build:
> - `stg_scooter_telemetry`: clean & rename fields  
> - `fct_scooter_kpis`:  
>     - avg battery at ride end  
>     - % scooters ending rides < 20%  
>     - top idle locations (via GPS clustering)  
>  
> Push models + `schema.yml` tests/docs to GitHub. We’ll demo to Zippy soon.

### Deliverables  
- [ ] Init dbt project under `/dbt_project/`  
- [ ] Create `stg_scooter_telemetry.sql`  
- [ ] Create `fct_scooter_kpis.sql`  
- [ ] Add `schema.yml` with tests + docs  
- [ ] Run locally and validate output  
- [ ] Review with Ravi via Slack