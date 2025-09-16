# Data Science Portfolio

This repository contains a comprehensive collection of data science assignments and projects, showcasing various techniques in data analysis, visualization, and machine learning.

## Repository Structure

```
data-science/
├── assignments/           # All assignment notebooks organized by topic
│   ├── house_sales_analysis/     # King County house sales prediction
│   ├── automobile_sales_visualization/  # Automobile sales dashboard
│   └── spacex_data_analysis/     # SpaceX data wrangling project
├── data/                 # Datasets used in assignments
├── scripts/              # Python utility scripts for automation
├── outputs/              # Generated outputs and results
│   └── screenshots/      # Screenshot collections for assignments
└── README.md            # This file
```

## Assignments Overview

### 1. House Sales Analysis (King County, USA)
**File:** `assignments/house_sales_analysis/House_Sales_in_King_Count_USA.ipynb`

A comprehensive data analysis and machine learning project analyzing house sales in King County. This assignment covers:
- **Questions 1-10:** Complete peer-review assignment with code and analysis
- **Data Exploration:** Statistical analysis, correlations, and visualizations
- **Machine Learning Models:** Linear regression, Ridge regression, polynomial features
- **Model Evaluation:** R² scores, cross-validation, train/test splits
- **Visualizations:** Scatter plots, box plots, regression plots

**Key Results:**
- Single feature R² scores: sqft_living (0.493), grade (0.467)
- Multiple features R² (11 features): 0.658
- Pipeline with polynomial features: Advanced model evaluation
- Ridge regression with regularization for overfitting prevention

### 2. Automobile Sales Visualization
**File:** `assignments/automobile_sales_visualization/Automobile_Sales_Data_Visualization.ipynb`

Interactive dashboard and visualization project for automobile sales data:
- **Part 1:** Plotly visualizations (line charts, bar charts, pie charts, scatter plots)
- **Part 2:** Interactive Dash web application with dropdown menus and dynamic plotting
- **Dashboard Features:** Year-wise statistics, recession period analysis, sales trends

### 3. SpaceX Data Analysis
**File:** `assignments/spacex_data_analysis/spacex_data_wrangling_completed.ipynb`

Data wrangling and preprocessing project for SpaceX launch data:
- Data cleaning and transformation
- Feature engineering and analysis
- Exploratory data analysis with visualizations

## Generated Outputs

### Screenshots
All assignment screenshots are organized in `outputs/screenshots/`:
- `house_sales/`: 10 question screenshots for peer review submission
- `automobile_sales/`: Dashboard and visualization screenshots

## Technical Stack

### Libraries Used
- **Data Analysis:** pandas, numpy
- **Machine Learning:** scikit-learn (LinearRegression, Ridge, PolynomialFeatures, Pipeline)
- **Visualization:** matplotlib, seaborn, plotly
- **Web Dashboard:** dash, plotly.graph_objects
- **Development:** jupyter notebook, python 3.13

### Environment Setup
```bash
# Create virtual environment
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install pandas numpy scikit-learn matplotlib seaborn plotly dash jupyter
```

## How to Run

### Individual Assignments
1. Navigate to the assignment folder
2. Open the Jupyter notebook
3. Run all cells sequentially

### House Sales Analysis
```bash
cd assignments/house_sales_analysis
jupyter notebook House_Sales_in_King_Count_USA.ipynb
```

### Automobile Sales Dashboard
```bash
cd assignments/automobile_sales_visualization
jupyter notebook Automobile_Sales_Data_Visualization.ipynb
```

## Dataset Information

### House Sales Dataset
- **File:** `data/kc_house_data_NaN.csv`
- **Records:** 21,613 house sales
- **Features:** 22 columns including price, bedrooms, bathrooms, sqft_living, etc.
- **Source:** King County public records

## Assignment Completion Status

✅ **House Sales Analysis:** Complete (all 10 questions + additional analysis)
- All code cells executed successfully
- R² scores calculated for various models
- Comprehensive visualizations generated
- Screenshots captured for peer review

✅ **Automobile Sales Visualization:** Complete (Parts 1 & 2)
- Interactive dashboard implemented
- All visualization types created
- Screenshots generated

✅ **SpaceX Data Analysis:** Complete
- Data wrangling and preprocessing finished

## Key Learning Outcomes

1. **Data Analysis:** Statistical analysis, correlation studies, feature selection
2. **Machine Learning:** Linear regression, regularization, model evaluation
3. **Visualization:** Creating effective plots for data storytelling
4. **Dashboard Development:** Interactive web applications with Dash
5. **Code Organization:** Jupyter notebook best practices and documentation

## Screenshots and Submission

All assignment screenshots are available in `outputs/screenshots/` for:
- Peer review submissions
- Portfolio demonstration
- Progress documentation

For questions or issues, please refer to the individual assignment README files in each folder.