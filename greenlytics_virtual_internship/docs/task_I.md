## Task 1: Data Discovery & Cleaning

### Overview
Lay the foundation for your entire project by loading, inspecting, and cleaning the raw datasets collected from IoT sensors and open sources in London.

### Problem Context
The raw data from January–March contains gaps, duplicates, and strange encodings due to sensor outages. Clean, trustworthy data is crucial before any modeling can begin.

### Tech Tools
- Python
- Excel
- SQL
- Pandas  
- Matplotlib
- Seaborn
- Plotly  
- Jupyter Notebooks  
- AWS S3  
- Slack + Zoom 

### Email from Anna

> **From:** Anna Vermeer  
> **Subject:** Welcome aboard + your first task  
> **To:** Intern  
>
> Hi,  
>
> Welcome to Greenlytics! We’re thrilled to have you join the Urban Insights Team.  
>
> London is one of our most engaged city partners, and the Mayor’s office is keen on using predictive tools to combat air pollution. That’s where your work comes in.  
>
> Your first task is to **prepare clean and trustworthy AQI data** for modeling. Miguel will give you access to our raw sensor feeds, which include:
>
> - Air Quality Index (AQI)  
> - PM2.5, NO₂, and CO levels  
> - Temperature and wind speed  
> - Traffic congestion scores  
>
> Expect **gaps**, **duplicates**, and some **funky encodings**, especially in January and February.  
>
> Once the data is cleaned, please generate an **Exploratory Data Analysis (EDA) report** that includes:
>
> - Time series trends  
> - Missing data visualizations  
> - Outlier detection  
> - Early correlations between features and AQI  
>
> Post your findings in the `#urban-insights` Slack channel and book a **15-minute readout** with me by next Friday to walk through your insights.  
>
> Let me know if you hit any blockers!  
>
> Best,  
> Anna

### Slack DM from Miguel Ortega

> Hey, welcome to Greenlytics  
>
> I've set up your access to the London raw sensor data.  
> You’ll find everything in this S3 bucket:  
> `s3://greenlytics-data/london/raw/`  
>
> Heads up — sensors glitched quite a bit in **January and February**, so you'll likely spot missing values or sudden spikes. If anything looks suspicious or inconsistent, ping me directly and I’ll help debug.  
>
> Also, let me know if you need help pulling the files into your notebook environment.  
>
> Cheers,  
> Miguel

### Deliverables
- [ ] Load and inspect raw AQI, weather, and traffic data  
- [ ] Clean and preprocess the datasets (handle missing values, duplicates, format issues)  
- [ ] Create an EDA notebook/report covering:
  - Data completeness and quality issues  
  - Key feature distributions and trends  
  - Anomalies and outliers  
  - Any emerging patterns (daily, weekly, by zone)  
- [ ] Share a summary in Slack  
- [ ] Schedule and lead a 15-minute readout with Anna
