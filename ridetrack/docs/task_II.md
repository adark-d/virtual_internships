## Task 2: Stream Processing with Spark

### Overview  
Consume raw Kafka messages using Spark Structured Streaming, clean and enrich them, and write to PostgreSQL.

### Problem Context  
Paris ops teams need reliable data for dashboards. This task ensures telemetry is parsed, deduplicated, and cleaned before entering the warehouse.

### Tech Tools  
- PySpark  
- Spark Structured Streaming  
- PostgreSQL  
- Docker Compose  
- GitHub  

### Email from Erik Mensah

> **From:** Erik Mensah  
> **Subject:** Streaming Job Time!  
>  
> Connect Kafka to Spark. Your job should:  
> - Parse JSON from topic `zippy.paris.rides`  
> - Drop duplicate `scooter_id + timestamp`  
> - Fill missing `battery` values  
> - Calculate 2-min rolling battery average per scooter  
> Output to: PostgreSQL table `scooter_telemetry`

### Slack DM from Ravi Patel

> Once the table is in Postgres, I’ll connect it to dbt and Power BI.

### Deliverables  
- [ ] `spark_streaming_job.py`: read from Kafka, clean data  
- [ ] Deduplicate using `scooter_id + timestamp`  
- [ ] Fill nulls, compute rolling battery stats  
- [ ] Write cleaned data to PostgreSQL  
- [ ] Push logs to `/logs/`, code to `/spark_jobs/`