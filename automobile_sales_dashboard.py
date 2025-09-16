#!/usr/bin/env python3
"""
Automobile Sales Statistics Dashboard
Final Assignment - Part 2

This dashboard provides insights into automobile sales data with two main reports:
1. Yearly Automobile Sales Statistics
2. Recession Period Statistics
"""

import pandas as pd
import numpy as np
import dash
from dash import dcc, html, Input, Output
import plotly.express as px
from datetime import datetime, timedelta
import warnings
warnings.filterwarnings('ignore')

# Initialize the Dash app
app = dash.Dash(__name__)

# Create sample automobile sales dataset (enhanced for dashboard requirements)
np.random.seed(42)

# Create date range from 1980 to 2013 (as per requirements)
start_date = datetime(1980, 1, 1)
end_date = datetime(2013, 12, 31)
date_range = pd.date_range(start_date, end_date, freq='M')

# Define recession periods (historical US recessions between 1980-2013)
recession_periods = [
    (datetime(1980, 1, 1), datetime(1980, 7, 31)),    # 1980 recession
    (datetime(1981, 7, 1), datetime(1982, 11, 30)),   # 1981-82 recession
    (datetime(1990, 7, 1), datetime(1991, 3, 31)),    # 1990-91 recession
    (datetime(2001, 3, 1), datetime(2001, 11, 30)),   # 2001 recession
    (datetime(2007, 12, 1), datetime(2009, 6, 30))    # 2007-09 Great Recession
]

# Vehicle types as per dataset specification
vehicle_types = ['Supperminicar', 'Smallfamiliycar', 'Mediumfamilycar', 'Executivecar', 'Sports']

# Create the comprehensive dataset
data = []
for date in date_range:
    # Determine if in recession
    is_recession = any(start <= date <= end for start, end in recession_periods)
    
    for vehicle_type in vehicle_types:
        # Base sales influenced by recession, seasonality, and trends
        base_sales = np.random.normal(1000, 200)
        
        # Recession effect
        if is_recession:
            base_sales *= 0.6  # 40% reduction during recession
        
        # Seasonality effect (higher sales in spring/summer)
        seasonal_factor = 1 + 0.3 * np.sin(2 * np.pi * date.month / 12)
        base_sales *= seasonal_factor
        
        # Vehicle type popularity
        type_multiplier = {
            'Supperminicar': 0.8, 
            'Smallfamiliycar': 1.2, 
            'Mediumfamilycar': 1.5, 
            'Executivecar': 1.1, 
            'Sports': 0.7
        }
        base_sales *= type_multiplier[vehicle_type]
        
        # Ensure positive sales
        automobile_sales = max(100, int(base_sales))
        
        # Generate other variables
        gdp = np.random.normal(25000, 3000) * (0.9 if is_recession else 1.0)
        unemployment_rate = np.random.normal(8.5 if is_recession else 5.5, 1)
        unemployment_rate = max(3, min(15, unemployment_rate))
        
        # Consumer confidence
        consumer_confidence = np.random.normal(70 if not is_recession else 45, 10)
        consumer_confidence = max(20, min(100, consumer_confidence))
        
        # Seasonality weight
        seasonality_weight = 1 + 0.2 * np.sin(2 * np.pi * date.month / 12)
        
        # Price variations
        base_price = {
            'Supperminicar': 15000, 
            'Smallfamiliycar': 20000, 
            'Mediumfamilycar': 30000, 
            'Executivecar': 45000, 
            'Sports': 60000
        }
        price_variation = np.random.normal(1, 0.15)
        price = base_price[vehicle_type] * price_variation
        
        # Advertising expenditure
        base_ad_spend = np.random.normal(800000, 150000)
        if is_recession:
            base_ad_spend *= 0.7  # Reduced spending during recession
        advertising_expenditure = max(100000, base_ad_spend)
        
        # Competition measure
        competition = np.random.normal(5, 1.5)
        competition = max(1, min(10, competition))
        
        data.append({
            'Date': date,
            'Recession': 1 if is_recession else 0,
            'Automobile_Sales': automobile_sales,
            'GDP': gdp,
            'unemployment_rate': unemployment_rate,
            'Consumer_Confidence': consumer_confidence,
            'Seasonality_Weight': seasonality_weight,
            'Price': price,
            'Advertising_Expenditure': advertising_expenditure,
            'Vehicle_Type': vehicle_type,
            'Competition': competition,
            'Month': date.month,
            'Year': date.year
        })

# Create DataFrame
data = pd.DataFrame(data)

# Year list for dropdown
year_list = [i for i in range(1980, 2014, 1)]

# TASK 2.1: Create a Dash application and give it a meaningful title
app.layout = html.Div([
    html.H1("Automobile Sales Statistics Dashboard", 
            style={'textAlign': 'center', 'color': '#503D36', 'font-size': 24}),
    
    html.Div([
        html.Div([
            html.H2('Select Report Type:', style={'margin-right': '2em'}),
        ]),
        
        # TASK 2.2: Add drop-down menus to your dashboard with appropriate titles and options
        # Select Report-type Dropdown
        dcc.Dropdown(id='dropdown-statistics', 
                     options=[
                         {'label': 'Yearly Statistics', 'value': 'Yearly Statistics'},
                         {'label': 'Recession Period Statistics', 'value': 'Recession Period Statistics'}
                     ],
                     placeholder='Select a report type',
                     value='Select Statistics',
                     style={'width': '80%', 'padding': '3px', 'font-size': '20px', 'text-align-last': 'center'})
    ], style={'display': 'flex', 'align-items': 'center'}),
    
    html.Div([
        html.Div([
            html.H2('Select Year:', style={'margin-right': '2em'}),
        ]),
        
        # Select Year Dropdown
        dcc.Dropdown(id='select-year', 
                     options=[{'label': i, 'value': i} for i in year_list],
                     placeholder='Select-year',
                     value='Select-year',
                     style={'width': '80%', 'padding': '3px', 'font-size': '20px', 'text-align-last': 'center'})
    ], style={'display': 'flex', 'align-items': 'center'}),
    
    html.Br(),
    html.Br(),
    
    # TASK 2.3: Add a division for output display with appropriate id and classname property
    html.Div([
        html.Div(id='output-container', className='chart-grid', style={'display': 'flex'}),
    ])
])

# TASK 2.4: Creating Callbacks; Define the callback function to update the input container based on the selected statistics and the output container

# Update Input Container callback function
@app.callback(
    Output(component_id='select-year', component_property='disabled'),
    Input(component_id='dropdown-statistics', component_property='value'))
def update_input_container(selected_statistics):
    if selected_statistics == 'Yearly Statistics': 
        return False
    else: 
        return True

# Update Output Container callback function
@app.callback(
    Output(component_id='output-container', component_property='children'),
    [Input(component_id='dropdown-statistics', component_property='value'), 
     Input(component_id='select-year', component_property='value')])
def update_output_container(selected_statistics, input_year):
    
    # TASK 2.5: Create and display graphs for Recession Report Statistics
    if selected_statistics == 'Recession Period Statistics':
        # Filter the data for recession periods
        recession_data = data[data['Recession'] == 1]
        
        # Plot 1: Automobile sales fluctuate over Recession Period (year wise) using line chart
        # Grouping data for plotting
        yearly_rec = recession_data.groupby('Year')['Automobile_Sales'].mean().reset_index()
        # Plotting the line graph
        R_chart1 = dcc.Graph(
            figure=px.line(yearly_rec, 
                x='Year',
                y='Automobile_Sales',
                title="Average Automobile Sales fluctuation over Recession Period"))
        
        # Plot 2: Calculate the average number of vehicles sold by vehicle type and represent as a Bar chart
        # Use groupby to create relevant data for plotting. 
        average_sales = recession_data.groupby('Vehicle_Type')['Automobile_Sales'].mean().reset_index()                 
        R_chart2 = dcc.Graph(
            figure=px.bar(average_sales,
            x='Vehicle_Type',
            y='Automobile_Sales',
            title="Average Number of Vehicles Sold by Vehicle Type"))
        
        # Plot 3: Pie chart for total expenditure share by vehicle type during recessions
        # Grouping data for plotting
        exp_rec = recession_data.groupby('Vehicle_Type')['Advertising_Expenditure'].sum().reset_index()
        R_chart3 = dcc.Graph(
            figure=px.pie(exp_rec,
                values='Advertising_Expenditure',
                names='Vehicle_Type',
                title="Total Expenditure Share by Vehicle Type During Recessions"))
        
        # Plot 4: Develop a Bar chart for the effect of unemployment rate on vehicle type and sales
        # Grouping data for plotting
        unemp_data = recession_data.groupby(['unemployment_rate', 'Vehicle_Type'])['Automobile_Sales'].mean().reset_index()
        R_chart4 = dcc.Graph(figure=px.bar(unemp_data,
            x='unemployment_rate',
            y='Automobile_Sales',
            color='Vehicle_Type',
            labels={'unemployment_rate': 'Unemployment Rate', 'Automobile_Sales': 'Average Automobile Sales'},
            title='Effect of Unemployment Rate on Vehicle Type and Sales'))
        
        return [
            html.Div(className='chart-item', children=[html.Div(children=R_chart1), html.Div(children=R_chart2)], style={'display': 'flex'}),
            html.Div(className='chart-item', children=[html.Div(children=R_chart3), html.Div(children=R_chart4)], style={'display': 'flex'})
        ]
    
    # TASK 2.6: Create and display graphs for Yearly Report Statistics
    # Yearly Statistic Report Plots 
    # Check for Yearly Statistics.
    elif (input_year and selected_statistics == 'Yearly Statistics'):
        yearly_data = data[data['Year'] == input_year]
        
        # Plot 1: Yearly Automobile sales using line chart for the whole period.
        # Grouping data for plotting.
        yas = data.groupby('Year')['Automobile_Sales'].mean().reset_index()
        Y_chart1 = dcc.Graph(figure=px.line(yas, x='Year', y='Automobile_Sales', title='Yearly Automobile Sales for the Whole Period'))
        
        # Plot 2: Total Monthly Automobile sales using line chart.
        # Grouping data for plotting.
        mas = yearly_data.groupby('Month')['Automobile_Sales'].sum().reset_index()
        Y_chart2 = dcc.Graph(figure=px.line(mas,
            x='Month',
            y='Automobile_Sales',
            title='Total Monthly Automobile Sales'))
        
        # Plot bar chart for average number of vehicles sold during the given year
        # Grouping data for plotting.
        avr_vdata = yearly_data.groupby('Vehicle_Type')['Automobile_Sales'].mean().reset_index()
        Y_chart3 = dcc.Graph(figure=px.bar(avr_vdata, x='Vehicle_Type', y='Automobile_Sales', title='Average Vehicles Sold by Vehicle Type in the year {}'.format(input_year)))
        
        # Plot 4: Total Advertisement Expenditure for each vehicle using pie chart
        # Grouping data for plotting.
        exp_data = yearly_data.groupby('Vehicle_Type')['Advertising_Expenditure'].sum().reset_index()
        Y_chart4 = dcc.Graph(
            figure=px.pie(exp_data, 
            values='Advertising_Expenditure',
            names='Vehicle_Type',
            title='Total Advertisement Expenditure for Each Vehicle'))
        
        return [
            html.Div(className='chart-item', children=[html.Div(children=Y_chart1), html.Div(children=Y_chart2)], style={'display':'flex'}),
            html.Div(className='chart-item', children=[html.Div(children=Y_chart3), html.Div(children=Y_chart4)], style={'display': 'flex'})
        ]
    
    else:
        return None

# Run the app
if __name__ == '__main__':
    app.run(debug=True, port=8050)