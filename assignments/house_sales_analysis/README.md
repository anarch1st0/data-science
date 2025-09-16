# House Sales Analysis - King County, USA

This notebook contains a comprehensive data analysis and machine learning project for predicting house sales prices in King County, Washington.

## Assignment Overview

This is a peer-reviewed assignment consisting of 10 main questions covering various aspects of data science:

### Question 1: Data Types and Missing Values
- Display data types for all columns
- Check for missing values in the dataset

### Question 2: Statistical Summary
- Generate descriptive statistics for numerical columns
- Analyze data distribution and ranges

### Question 3: Data Visualization - House Prices
- Create visualizations showing house price distributions
- Analyze price patterns and outliers

### Question 4: Feature Analysis - Bedrooms
- Explore the relationship between number of bedrooms and house prices
- Statistical analysis of bedroom counts

### Question 5: Correlation Analysis - Bathrooms
- Calculate correlation between bathrooms and house prices
- Visualize the relationship with scatter plots

### Question 6: Feature Analysis - Floors
- Analyze the impact of number of floors on house prices
- Compare price distributions across different floor counts

### Question 7: Correlation Analysis - Multiple Features
- Calculate correlations between multiple features and house prices
- Identify the most predictive features for price

### Question 8: Linear Regression - Single Feature
- Build linear regression model using sqft_living
- Calculate R² score and evaluate model performance

### Question 9: Linear Regression - Multiple Features
- Build regression model using multiple features
- Compare performance with single-feature model

### Question 10: Ridge Regression with Polynomial Features
- Implement Ridge regression with polynomial feature transformation
- Evaluate model performance and compare with linear models

## Technical Implementation

### Libraries Used
```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression, Ridge
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
```

### Dataset Information
- **File:** `../../data/kc_house_data_NaN.csv`
- **Records:** 21,613 house sales
- **Features:** 22 columns including:
  - `price`: Target variable (house price)
  - `bedrooms`, `bathrooms`: Number of rooms
  - `sqft_living`, `sqft_lot`: Square footage measurements
  - `floors`: Number of floors
  - `waterfront`: Waterfront property indicator
  - `view`: View rating (0-4)
  - `condition`: Overall condition (1-5)
  - `grade`: Overall grade (1-13)
  - `lat`, `long`: Geographic coordinates

### Key Results

#### Correlation Analysis
- **Most correlated with price:** sqft_living (0.702)
- **Strong predictors:** grade (0.667), sqft_above (0.606)
- **Moderate predictors:** bathrooms (0.525), view (0.397)

#### Model Performance (R² Scores)
1. **Single Feature (sqft_living):** 0.493
2. **Multiple Features (11 features):** 0.658
3. **Ridge Regression:** Optimized with regularization
4. **Polynomial Features:** Enhanced feature engineering

#### Feature Coefficients (Multiple Regression)
- `waterfront`: $602,135 (highest impact)
- `lat`: $672,896 (location premium)
- `grade`: $82,845 (quality impact)
- `sqft_living`: $129.39 per sq ft

## How to Run

1. **Open the notebook:**
   ```bash
   jupyter notebook House_Sales_in_King_Count_USA.ipynb
   ```

2. **Run all cells sequentially** - The notebook is designed to run from top to bottom

3. **Data loading:** The notebook automatically loads data from `../../data/kc_house_data_NaN.csv`

## Assignment Completion

✅ **All 10 Questions Completed**
- Each question includes complete code implementation
- Results are clearly displayed with explanations
- Visualizations included where appropriate

✅ **Additional Analysis**
- Extended correlation analysis
- Multiple regression implementations
- Pipeline setup with polynomial features
- Ridge regression with train/test splits

✅ **Screenshots Generated**
- All question outputs captured for peer review
- Screenshots available in `../../outputs/screenshots/house_sales/`

## Code Quality Features

- **Error Handling:** Robust data loading with fallbacks
- **Documentation:** Clear markdown explanations for each section
- **Visualization:** Professional plots with proper labels and formatting
- **Modular Code:** Reusable functions and clear variable naming
- **Performance:** Efficient pandas operations and scikit-learn usage

## Learning Objectives Achieved

1. **Data Exploration:** Comprehensive EDA with statistics and visualizations
2. **Feature Engineering:** Correlation analysis and feature selection
3. **Machine Learning:** Linear and Ridge regression implementation
4. **Model Evaluation:** R² scores, train/test splits, and performance comparison
5. **Python Skills:** Pandas, NumPy, scikit-learn, and matplotlib proficiency

## Peer Review Submission

This notebook is ready for peer review with:
- Complete answers to all 10 questions
- Clear code with comments and explanations
- Professional visualizations and results
- Screenshots available for grading rubric

For any questions about the implementation or results, please refer to the code comments and markdown explanations throughout the notebook.