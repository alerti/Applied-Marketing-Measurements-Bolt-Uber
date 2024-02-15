Bolt – Senior Data Analyst, Applied Marketing Measurements 
==============================

Marketting decision analysis 


## Analysis Steps:

### Understand the Dataset:
- Load the dataset into a Python  notebook and explore its structure and content.
- Check for missing values, outliers, and any data preprocessing requirements.

### Define Key Metrics:
- Identify the key performance indicators (KPIs) relevant to the campaign, such as the number of rides, cost per ride (CPA), and cost per thousand impressions (CPM).

### Benchmarking:
- Compare industry benchmarks for CPA and CPM with the suggested benchmarks from TweetX.
- Use this information to set realistic targets for the campaign.

### Budget Estimation:
- Based on the industry benchmarks and the suggested measurement design, estimate the budget required for the campaign.
- Consider factors like the number of impressions needed, expected click-through rates, and conversion rates.

### ROI Analysis:
- Calculate the potential return on investment (ROI) by estimating the revenue generated from the expected increase in rides and comparing it to the campaign cost.

### Spatial Analysis:
- Analyze the dataset for different cities to identify potential target locations for the TweetX campaign. Consider launching in cities where Bolt has a strong presence or high growth potential.

### Temporal Analysis:
- Explore the dataset over time to identify patterns and trends. Consider seasonality and other temporal factors that might influence the success of the campaign.

### Sensitivity Analysis:
- Perform sensitivity analysis on key variables, such as CPA, CPM, and the budget. Assess how changes in these variables impact the overall success of the campaign.

### Recommendations and Summary:
- Provide clear recommendations based on the analysis, including the suggested budget, measurement design, and potential impact on Bolt's growth in Poland.
- Summarize key findings for stakeholders, ensuring clarity for both data analytics experts and non-experts.

## Additional Assumptions:

### Assumptions on Conversion Rates:
- Make assumptions about the conversion rates from impressions to rides based on industry standards or any available data.

### Assumptions on User Behavior:
- If data on user behavior is not provided, make assumptions about how users might respond to the TweetX campaign.
```

Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io


--------

