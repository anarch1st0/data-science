"""
Task 2.4: Callback Functions Code Screenshot
This file shows the code snippet for creating the callback functions
"""

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
    
    if selected_statistics == 'Recession Period Statistics':
        # Filter the data for recession periods
        recession_data = data[data['Recession'] == 1]
        # ... rest of the recession plots code ...
        
    elif (input_year and selected_statistics == 'Yearly Statistics'):
        yearly_data = data[data['Year'] == input_year]
        # ... rest of the yearly plots code ...
        
    else:
        return None