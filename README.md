## Project of Advanced Coding for Data Analytics: Credit Score Data Analytics

### Project Overview
This project focuses on analysing and preparing a **credit score dataset** containing both **categorical and continuous variables**, with a strong emphasis on handling **dirty data** such as incorrect formatting, inconsistent values, and extensive missing values. :contentReference[oaicite:0]{index=0}

### Methodologies Used
- **Data Cleaning**
  - Fixed invalid entries (e.g., corrupted SSN values)
  - Standardised text fields (removed special characters/whitespace)
  - Restructured `Type_of_Loan` into cleaner formats
  - Converted columns into correct datatypes
  - Replaced placeholder values like `_` and `NM` with `NULL` before imputation :contentReference[oaicite:1]{index=1}

- **Handling Inconsistent Data**
  - Detected inconsistent values per customer using the **mode**
  - Replaced non-mode values with `NULL` for consistency :contentReference[oaicite:2]{index=2}

- **Imputation Strategy**
  - Used **rolling calendar logic (Jan–Aug)** for time-aware forward/backward filling of consistent fields (e.g., occupation, credit mix) :contentReference[oaicite:3]{index=3}
  - Applied **KNN Imputation** for inconsistent columns where values vary across time :contentReference[oaicite:4]{index=4}
  - Applied logical imputations (e.g., `Annual_Income = Monthly_Inhand_Salary × 12`)
  - Corrected negative delay-related fields by replacing them with **0** :contentReference[oaicite:5]{index=5}

- **Outlier Removal**
  - Identified and removed extreme/invalid values during iterative cleaning :contentReference[oaicite:6]{index=6}

- **Class Imbalance Handling**
  - Addressed imbalance in the target variable using **SMOTE** :contentReference[oaicite:7]{index=7}

- **Model Training & Evaluation**
  - Trained multiple classifiers:
    - Logistic Regression
    - Random Forest
    - XGBoost
    - Gradient Boosting :contentReference[oaicite:8]{index=8}

- **Bias Detection & Removal**
  - Used feature importance to identify bias (notably in **City** and **Age**)
  - Dropped biased features and retrained models for more realistic performance :contentReference[oaicite:9]{index=9}

### Outputs / Deliverables
- A fully cleaned and imputed dataset with improved consistency across customer timelines
- Classification models with performance:
  - ~0.98 accuracy before bias removal
  - ~0.76–0.81 accuracy after removing biased features (more realistic performance) :contentReference[oaicite:10]{index=10}
- A **Streamlit interface** demonstrating the final workflow and results :contentReference[oaicite:11]{index=11}
