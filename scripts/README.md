# Utility Scripts

This folder contains Python utility scripts for automating various tasks across the data science assignments.

## Script Overview

### Screenshot Generation Scripts

#### `create_house_sales_screenshots.py`
Automated screenshot generator for the House Sales assignment:
- **Purpose:** Capture screenshots of all 10 assignment questions
- **Output:** PNG files for peer review submission
- **Features:** Automatic code execution and output capture
- **Location:** Saves to `../outputs/screenshots/house_sales/`

#### `create_code_screenshots.py`
General-purpose screenshot utility for code cells:
- **Purpose:** Capture code and output from Jupyter notebooks
- **Features:** Customizable cell selection and formatting
- **Usage:** Flexible screenshot generation for any notebook

#### `create_dashboard_screenshots.py`
Dashboard visualization screenshot tool:
- **Purpose:** Capture interactive dashboard outputs
- **Features:** Automated browser screenshots and chart captures
- **Usage:** Document dashboard functionality and layouts

#### `create_enhanced_task2_screenshots.py`
Enhanced screenshot generator for specific assignment tasks:
- **Purpose:** Advanced screenshot capabilities with annotations
- **Features:** Multi-panel captures and enhanced formatting
- **Usage:** Professional presentation-ready screenshots

#### `take_screenshots.py`
Basic screenshot utility:
- **Purpose:** Simple screenshot capture functionality
- **Features:** Basic image capture and saving
- **Usage:** Quick screenshot generation for documentation

### Dashboard and Visualization Scripts

#### `automobile_sales_dashboard.py`
Standalone dashboard application:
- **Purpose:** Run automobile sales dashboard independently
- **Features:** Complete Dash web application
- **Usage:** Deploy dashboard without Jupyter notebook
- **Access:** Runs on `http://127.0.0.1:8050/`

#### `task_2_3_code.py`
Specific task implementation:
- **Purpose:** Standalone code for assignment task 2.3
- **Features:** Modular implementation of specific requirements
- **Usage:** Independent execution of task components

#### `task_2_4_code.py`
Specific task implementation:
- **Purpose:** Standalone code for assignment task 2.4
- **Features:** Modular implementation of specific requirements
- **Usage:** Independent execution of task components

### Temporary Files

#### `tempCodeRunnerFile.python`
Temporary execution file:
- **Purpose:** VS Code Python execution cache
- **Note:** Auto-generated file, safe to ignore/delete

## Usage Instructions

### Running Screenshot Scripts
```bash
# Navigate to scripts folder
cd scripts/

# Run specific screenshot generator
python create_house_sales_screenshots.py

# Run dashboard screenshot capture
python create_dashboard_screenshots.py
```

### Running Dashboard Independently
```bash
# Start automobile sales dashboard
python automobile_sales_dashboard.py

# Access at: http://127.0.0.1:8050/
```

### Script Dependencies
Most scripts require:
```bash
pip install pandas numpy matplotlib seaborn plotly dash jupyter
```

## Script Features

### Automation Benefits
- **Time Saving:** Automated screenshot generation for all assignments
- **Consistency:** Standardized formatting and layout
- **Quality:** Professional presentation-ready outputs
- **Batch Processing:** Generate multiple screenshots efficiently

### Professional Standards
- **Error Handling:** Robust error checking and recovery
- **Documentation:** Clear comments and usage instructions
- **Modularity:** Reusable functions and components
- **Flexibility:** Configurable options and parameters

### Output Management
- **Organized Storage:** Screenshots saved in logical folder structure
- **Naming Conventions:** Consistent and descriptive file names
- **Format Standards:** High-quality PNG outputs
- **Batch Operations:** Efficient processing of multiple files

## Customization

### Screenshot Settings
Most scripts allow customization of:
- **Output Resolution:** Adjust image size and quality
- **File Naming:** Custom naming patterns and conventions
- **Save Locations:** Flexible output directory configuration
- **Content Selection:** Choose specific cells or sections to capture

### Dashboard Configuration
Dashboard scripts support:
- **Port Configuration:** Change default port settings
- **Theme Customization:** Modify visual appearance
- **Data Sources:** Connect to different datasets
- **Feature Toggles:** Enable/disable specific functionality

## Development Notes

### Code Quality
- **Python Standards:** Following PEP 8 style guidelines
- **Error Handling:** Comprehensive exception management
- **Performance:** Optimized for large datasets and batch operations
- **Maintainability:** Clear structure and documentation

### Testing
Scripts have been tested with:
- **Multiple Operating Systems:** macOS, Windows, Linux compatibility
- **Various Python Versions:** Python 3.8+ support
- **Different Data Sizes:** Scalable for various dataset sizes
- **Browser Compatibility:** Cross-browser dashboard support

## Troubleshooting

### Common Issues
1. **Import Errors:** Ensure all dependencies are installed
2. **Path Issues:** Check file paths and working directories
3. **Permission Errors:** Verify write permissions for output folders
4. **Browser Issues:** For dashboard scripts, ensure browser availability

### Getting Help
- Check script comments for usage instructions
- Verify all dependencies are properly installed
- Ensure proper file paths and permissions
- Review error messages for specific guidance

These scripts significantly enhance productivity and maintain professional standards across all data science assignments and projects.