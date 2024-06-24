import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import os
import time
import keyboard

# Initialize the webdriver
service = ChromeService(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Function to extract data and save to CSV
def extract_data_to_csv():
    # Example: extracting table data
    table = driver.find_element(By.TAG_NAME, "table")
    rows = table.find_elements(By.TAG_NAME, "tr")
    
    data = []
    for row in rows:
        cols = row.find_elements(By.TAG_NAME, "td")
        data.append([col.text for col in cols])
    
    # Convert data to DataFrame and save as CSV
    df = pd.DataFrame(data)
    output_path = os.path.join(os.getcwd(), "extracted_data.csv")
    df.to_csv(output_path, index=False)
    print(f"Data extracted to {output_path}")

# Open the website
driver.get("https://na.delphi.iscore.a2z.com/planning/near-real-time-inventory")
print("Navigate to the webpage and press 'u' to extract data to CSV.")

# Wait for user input
keyboard.wait('u')
extract_data_to_csv()

# Close the browser
driver.quit()
