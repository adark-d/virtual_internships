## Task 2: Feature Engineering & Baseline Modeling

### Overview
Transform raw data into meaningful features and train your first AQI forecasting model to get a performance benchmark.

### Problem Context
To predict AQI accurately, you need to engineer relevant features like prior pollution levels, weather conditions, and time-based factors. This will help capture temporal and environmental trends.

### Tech Tools
- Python
- Pandas
- Numpy
- Scikit-learn
- Plotly
- Matplotlib
- Seaborn
- Jupyter Notebooks
- GitHub
- Slack

### Email from Ravi

> **From:** Dr. Ravi Kapoor  
> **Subject:** Feature crafting for AQI model  
> **To:** Intern  
>
> Hey,  
>
> Great work on the data cleaning and EDA — your insights around **weekday vs. weekend NO₂ levels** were spot on.  
>
> Let’s start engineering features for the AQI forecasting model. I recommend experimenting with:
>
> - **Lag features**: Prior-day or prior-hour values of AQI, NO₂, traffic, etc.  
> - **Interaction terms**: Combinations like `temperature × wind_speed`, or `traffic × time_of_day`  
> - **Categorical encoding**: Convert features like `hour of day`, `day of week`, and `school holidays` into usable inputs  
>
> Once your features are ready, run a **Random Forest Regressor** as a baseline. Use `train_test_split()` to create a holdout set. Track key metrics:  
>
> - **Root Mean Squared Error (RMSE)**  
> - **Mean Absolute Error (MAE)**  
>
> Push your code to the `model_dev` branch and tag me in the PR when you're done.  
>
> Good luck — keep things interpretable!

### Slack Thread in `#data-science-interns`

> **You:**  
> "Should I normalize traffic volume or weather features before feeding them into the model?"  
>
> **Ravi:**  
> "No need — tree-based models like Random Forests are scale-invariant. But document your decision."

### Deliverables
- [ ] Engineer relevant features from the cleaned dataset:
  - Lagged variables
  - Encoded time-based categories
  - Interaction terms
- [ ] Train a **Random Forest baseline model**
  - Use `train_test_split()` from `scikit-learn`
  - Log RMSE and MAE on validation set
- [ ] Document model results in `results.md` (include feature importance)
- [ ] Push your work to the `model_dev` GitHub branch and tag Ravi
- [ ] Open a GitHub issue titled:  
  **“Baseline model: What’s working / what’s not”**  
  Summarize early observations and possible next steps
