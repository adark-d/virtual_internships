## Task 4: Model Deployment via API

### Overview
Make your model accessible to other systems by wrapping it in a production-ready REST API using FastAPI.

### Problem Context
Forecasts need to be consumed by the Greenlytics platform and potentially external dashboards. An API ensures your model can be called reliably and repeatedly.

### Tech Tools
- FastAPI  
- Uvicorn
- Docker
- ZenML
- Mlflow  
- GitHub

### Slack Thread in `#project-demo`

> **Miguel:**  
> "Use the base Dockerfile from `greenlytics-deploy-template` to containerize your app. Let me know if local testing gives you any trouble."  
>
> **You:**  
> "Thanks! Just deployed the FastAPI service — predictions are working. Hooking it into the Streamlit dashboard tomorrow."

### Deliverables
- [ ] **Deploy the trained model using FastAPI**
  - Create a `/predict` endpoint that accepts input features and returns AQI predictions
  - Ensure it works locally and is containerized using Docker
