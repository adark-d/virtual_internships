# RideTrack Internship Setup Guide

Welcome to your Data Engineering internship at RideTrack!

This project simulates a real-world scooter fleet data pipeline using Kafka, Spark, PostgreSQL, and Power BI.


## Getting Started

### 1. Clone the Project
```bash
git clone https://github.com/your-org/ridetrack-internship.git
cd ridetrack-internship
```

### 2. Start Kafka and Zookeeper
```bash
docker-compose up -d
```

### 3. Simulate Scooter Data Stream
```bash
poetry install  # or pip install -r requirements.txt
python kafka_producer.py
```

### 4. Optional: Preview Static Data
You can use `mock_stream_output.csv` if your Kafka setup is not working:
```bash
head -n 5 mock_stream_output.csv
```


## Testing the Pipeline

- Build your Spark job to consume from topic `zippy.paris.rides`
- Write outputs to PostgreSQL
- Use `dbt` to transform the telemetry data
- Visualize final KPIs using Power BI

Good luck!