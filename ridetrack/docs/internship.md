# Virtual Internship: Real-Time Data Engineering at RideTrack

---

# About RideTrack

**RideTrack** is a Berlin-based **smart mobility startup** that helps e-scooter operators across Europe optimize fleet performance using real-time telemetry and advanced analytics. Our mission is to help urban operators **minimize downtime**, **maximize battery life**, and **streamline fleet logistics** through data.

At the heart of our platform is a streaming data pipeline that ingests **high-frequency telemetry data** from thousands of e-scooters. This includes ride sessions, battery levels, error codes, and geolocation pings. We process these streams in real-time using **Kafka and Spark Structured Streaming**, enabling city teams to monitor scooter health, track utilization, and respond quickly to issues on the ground.

We’ve deployed our platform with leading operators in Berlin, Warsaw, and Amsterdam. Most recently, we partnered with **Zippy Scooters**, a fast-growing operator in **Paris**, to power their fleet’s real-time intelligence and operational insights.

---

## Tech Stack

- **Streaming & Processing**: Apache Kafka, Spark Structured Streaming  
- **Data Engineering & Workflow**: Python, Airflow, Docker  
- **Data Storage & Modeling**: PostgreSQL, dbt  
- **Business Intelligence**: Power BI  
- **Cloud & DevOps**: Confluent (Kafka), AWS (S3, RDS), GitHub, Slack  

---

## Our Team

We are a cross-functional team of:

- Product Managers focused on fleet efficiency and user experience  
- Data Engineers building scalable telemetry pipelines  
- Analytics Engineers enabling downstream insights and dashboards  
- Mobility Analysts who translate real-time metrics into operational wins  

We work in **agile squads**, with fast feedback loops across data, product, and operations.

---

## Our Culture

At RideTrack, we believe in:

- **Remote-first collaboration**: Async-friendly and globally distributed  
- **Sustainability in motion**: Our work supports cleaner, smarter mobility  
- **Operational impact**: Every pipeline, metric, and alert serves real-time decision-making  
- **Autonomy + mentorship**: You’ll own your deliverables, but you won’t be alone

---

## Internship Story: Welcome to the Team

You’ve just joined **RideTrack** as a **Data Engineering Intern** on the **Platform Engineering Team**.

It’s your first day—and it’s a busy one. We’ve just signed Zippy Scooters in **Paris**, and your task is critical: Zippy’s operations team needs real-time visibility into their scooters' performance, and you’re going to build the pipeline that powers it.

Your six-week internship will simulate a real-world engineering sprint. You’ll be responsible for building a **fully containerized, production-ready telemetry data pipeline**. You’ll simulate live ride data, stream it through Kafka, transform it using Spark, and write it to PostgreSQL. From there, the analytics team will use dbt and Power BI to surface insights for Zippy’s field teams.

Your work will directly support battery health monitoring, scooter downtime reduction, and fleet availability tracking for one of the fastest-growing operators in France.

**What You'll Be Doing**

Over the course of your internship, you’ll:

- Simulate real-time scooter telemetry (ride sessions, battery levels, GPS)  
- Ingest and stream that data via **Apache Kafka**  
- Write Spark Structured Streaming jobs to process and clean incoming telemetry  
- Store processed data in a **PostgreSQL** warehouse  
- Collaborate with the analytics team to define **dbt models** and support dashboard development  
- Package everything in Docker to enable smooth local and production deployment

**You'll Be Working With**

- **Marta Kruger**, *Product Manager*  
  - Defines KPIs and use cases. She’ll help translate technical work into fleet-level value.

- **Erik Mensah**, *Lead Data Engineer*  
  - Your technical mentor. He’ll review your pipeline architecture, Spark code, and Docker setup.

- **Ravi Patel**, *Analytics Engineer*  
  - Builds Power BI dashboards using your pipeline outputs. He’ll advise on schema design and table readiness.

**Communication & Workflow**

- **Tools**: GitHub (code), Slack (daily syncs), Notion (project tracker), Zoom (1:1s & reviews)  
- **Sprint Rhythm**: Weekly sprint planning on Mondays, async demos on Fridays  
- **Mentorship**: 1:1 with Erik every Tuesday afternoon  
- **Final Demo**: You’ll present your full pipeline on Week 6 to the RideTrack team and Zippy Scooters leadership

You're not just here to write code—you’re here to help **power a city’s entire scooter network in real-time**. Let’s build something great.

---

## Internship Goal

As a Data Engineering Intern at RideTrack, your goal is to design, simulate, and deploy a real-time streaming pipeline that ingests and processes scooter telemetry from Zippy Scooters’ Paris fleet.

Your pipeline will serve as the foundation for Zippy’s fleet dashboards, alerts, and operational KPIs—and it will be packaged to scale to other cities in the future.

### Key Deliverables

By the end of your internship, you are expected to deliver:

- **Simulated Real-Time Scooter Telemetry**  
  A Python-based simulator that produces JSON ride events (with battery %, GPS, status) and streams them into Kafka topics at a realistic frequency.

- **Streaming Data Pipeline (Spark + Kafka)**  
  A Spark Structured Streaming job that reads from Kafka, parses and cleans incoming telemetry, enriches it (e.g., geozone tagging), and writes to PostgreSQL.

- **PostgreSQL Schema for Analytics**  
  Design and document the table structure to support downstream reporting, including ride sessions, battery performance, and usage summaries.

- **Dockerized Local Environment**  
  All pipeline components run reproducibly via Docker Compose—including Kafka, Spark, and PostgreSQL—for easy local testing and handoff.

- **Documentation & Readme**  
  A `README.md` explaining setup, architecture, and how to test and deploy the pipeline locally or in cloud environments.

- **Support for dbt & BI Integration**  
  Ensure cleaned data supports dbt transformations and can feed into Power BI dashboards used by the analytics team.

This internship simulates the **end-to-end data engineering lifecycle**—from raw event generation to stakeholder-ready insights. You'll think in terms of events, schemas, partitions, and table models—all while shipping code that makes micro-mobility smarter and more sustainable.
