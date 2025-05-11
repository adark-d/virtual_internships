## Task 1: Data Simulation & Kafka Producer

### Overview  
Simulate real-time scooter telemetry and stream it to Kafka. This is the foundation of your pipeline.

### Problem Context  
Zippy Scooters Paris has 500 scooters in the field. We need realistic ride and battery event data to simulate live operations for testing our downstream analytics pipeline.

### Tech Tools  
- Python (`random`, `faker`)  
- Apache Kafka  
- Docker Compose (`kafka-sim-template`)  
- GitHub for version control  

### Email from Marta Kruger

> **From:** Marta Kruger  
> **Subject:** Paris Kickoff – Let’s Get Streaming!  
>  
> Zippy Scooters just launched 500 scooters in Paris, and we need to simulate their telemetry feed.  
> Each event should include:  
> - `scooter_id`, `timestamp`, `lat`, `lon`, `battery`, `ride_status`  
> Stream to topic: `zippy.paris.rides` at ~2–3 events/sec.  
> Once it's live, Erik will help connect Spark downstream.

### Slack DM from Erik Mensah

> Use Python’s `faker` or `random`, and spin up Kafka via Docker.  
> Ping me if your producer can't connect to the broker.

### Deliverables  
- [ ] Python Kafka producer that emits scooter telemetry  
- [ ] Message format includes battery %, ride status, and GPS drift  
- [ ] Writes to Kafka topic `zippy.paris.rides`  
- [ ] Document setup in `README.md`  
- [ ] Code pushed to GitHub `/producers/`