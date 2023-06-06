import pandas as pd
import requests

#  URL for the data download
url = "https://raw.githubusercontent.com/Biuni/PokemonGO-Pokedex/master/pokedex.json"

# Send a GET request to download the data
response = requests.get(url)

# Checking if the request was successful
if response.status_code == 200:
    # Read the JSON data
    data = response.json()

    # Extract the 'pokemon' records from the data
    pokemon_data = data['pokemon']

    # Create a DataFrame from the extracted data
    df = pd.DataFrame(pokemon_data)

    # Define the desired columns
    columns = ['name', 'type', 'height', 'weight']

    # Select only the desired columns in the DataFrame
    df = df[columns]

    # Convert the DataFrame to Excel format and save it
    df.to_excel('pokemon_data.xlsx', index=False)
    print("Data has been converted and saved to 'pokemon_data.xlsx'")
else:
    print("Failed to download the data. Check the URL or try again later.")
