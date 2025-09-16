#!/usr/bin/env python3
"""
Create mock screenshots for Tasks 2.3 and 2.4 code snippets
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch
import numpy as np

def create_code_screenshot(title, code_text, filename, figsize=(12, 8)):
    """Create a screenshot-like image of code"""
    fig, ax = plt.subplots(figsize=figsize, facecolor='white')
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis('off')
    
    # Create a code editor background
    code_bg = FancyBboxPatch((0.5, 2), 9, 6, 
                             boxstyle="round,pad=0.1", 
                             facecolor='#f8f8f8', 
                             edgecolor='#cccccc',
                             linewidth=1)
    ax.add_patch(code_bg)
    
    # Add title
    ax.text(5, 9, title, fontsize=16, fontweight='bold', ha='center', va='center')
    
    # Add code text
    ax.text(1, 5, code_text, fontsize=10, fontfamily='monospace', 
            ha='left', va='center', wrap=True)
    
    plt.tight_layout()
    plt.savefig(filename, dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()
    print(f"✅ Created: {filename}")

# Task 2.3: Output Division
task_2_3_code = """# TASK 2.3: Add a division for output display with appropriate id and classname property
html.Div([
    html.Div(id='output-container', className='chart-grid', style={'display': 'flex'}),
])"""

create_code_screenshot("Task 2.3: Output Division with ID and ClassName", 
                      task_2_3_code, "outputdiv.png")

# Task 2.4: Callbacks
task_2_4_code = """# TASK 2.4: Creating Callbacks

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
    # Callback implementation here
    pass"""

create_code_screenshot("Task 2.4: Callback Functions for Interactivity", 
                      task_2_4_code, "Callbacks.png", figsize=(14, 10))

print("\n🎯 Code screenshot files created successfully!")
print("📁 Files created:")
print("   • outputdiv.png")
print("   • Callbacks.png")