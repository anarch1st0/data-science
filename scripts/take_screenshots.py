#!/usr/bin/env python3
"""
Screenshot automation script for Dash Dashboard
This script takes all required screenshots for the assignment
"""

import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
import sys

def setup_driver():
    """Setup Chrome WebDriver with appropriate options"""
    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--window-size=1920,1080")
    
    try:
        driver = webdriver.Chrome(options=chrome_options)
        return driver
    except Exception as e:
        print(f"Error setting up Chrome driver: {e}")
        print("Please make sure ChromeDriver is installed and in PATH")
        return None

def take_screenshot(driver, filename, element_id=None):
    """Take screenshot of the entire page or specific element"""
    try:
        if element_id:
            element = driver.find_element(By.ID, element_id)
            element.screenshot(filename)
        else:
            driver.save_screenshot(filename)
        print(f"✅ Screenshot saved: {filename}")
        return True
    except Exception as e:
        print(f"❌ Error taking screenshot {filename}: {e}")
        return False

def main():
    print("🎯 Starting Dash Dashboard Screenshot Automation")
    print("="*60)
    
    # Setup WebDriver
    driver = setup_driver()
    if not driver:
        sys.exit(1)
    
    try:
        # Navigate to the dashboard
        driver.get("http://127.0.0.1:8050/")
        time.sleep(3)  # Wait for page to load
        
        # Task 2.1: Title screenshot
        print("📸 Task 2.1: Taking Title screenshot...")
        take_screenshot(driver, "Title.png")
        time.sleep(2)
        
        # Task 2.2: Dropdown screenshot
        print("📸 Task 2.2: Taking Dropdown screenshot...")
        take_screenshot(driver, "Dropdown.png")
        time.sleep(2)
        
        # Task 2.3: Output div screenshot (will take after creating the code)
        print("📸 Task 2.3: Output div will be captured via code screenshot")
        
        # Task 2.4: Callbacks screenshot (will take from code)
        print("📸 Task 2.4: Callbacks will be captured via code screenshot")
        
        # Task 2.5: Recession Report Statistics
        print("📸 Task 2.5: Taking Recession Report screenshots...")
        
        # Select Recession Period Statistics
        dropdown = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "dropdown-statistics"))
        )
        dropdown.click()
        time.sleep(1)
        
        # Click on Recession Period Statistics option
        recession_option = driver.find_element(By.XPATH, "//div[contains(text(), 'Recession Period Statistics')]")
        recession_option.click()
        time.sleep(3)  # Wait for graphs to load
        
        # Take screenshot of recession report graphs
        take_screenshot(driver, "RecessionReportgraphs.png")
        time.sleep(2)
        
        # Task 2.6: Yearly Report Statistics
        print("📸 Task 2.6: Taking Yearly Report screenshots...")
        
        # Select Yearly Statistics
        dropdown = driver.find_element(By.ID, "dropdown-statistics")
        dropdown.click()
        time.sleep(1)
        
        yearly_option = driver.find_element(By.XPATH, "//div[contains(text(), 'Yearly Statistics')]")
        yearly_option.click()
        time.sleep(2)
        
        # Select a year (e.g., 2010)
        year_dropdown = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "select-year"))
        )
        year_dropdown.click()
        time.sleep(1)
        
        # Select year 2010
        year_2010 = driver.find_element(By.XPATH, "//div[contains(text(), '2010')]")
        year_2010.click()
        time.sleep(3)  # Wait for graphs to load
        
        # Take screenshot of yearly report graphs
        take_screenshot(driver, "YearlyReportgraphs.png")
        
        print("\n🎉 All screenshots completed successfully!")
        print("📁 Files created:")
        print("   • Title.png")
        print("   • Dropdown.png") 
        print("   • RecessionReportgraphs.png")
        print("   • YearlyReportgraphs.png")
        
    except Exception as e:
        print(f"❌ Error during screenshot process: {e}")
    
    finally:
        driver.quit()
        print("🔒 Browser closed")

if __name__ == "__main__":
    main()