"""
Question 4 - Write a program to download the data from the link given below
and then read the data and convert the into the proper structure and return it as a CSV file.
Link - https://data.nasa.gov/resource/y77d-th95.json
"""

import pandas as pd
import requests

# Define the URL for data download
url = "https://data.nasa.gov/resource/y77d-th95.json"
# Send a GET request to download the data
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Read the JSON data
    data = response.json()

    # Create a DataFrame from the data
    df = pd.DataFrame(data)
        # Convert the DataFrame to CSV format and save it
    df.to_csv('nasa_data.csv', index=False)
    print("Data has been converted and saved to 'nasa_data.csv'")
else:
    print("Failed to download the data. Check the URL or try again later.")
