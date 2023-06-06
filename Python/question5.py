import requests

# Define the API URL for data download
url = "http://api.tvmaze.com/singlesearch/shows?q=westworld&embed=episodes"

# Send a GET request to download the data
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Extract the JSON data
    data = response.json()

    # Extract the show information
    show_name = data['name']
    show_genre = data['genres']
    show_summary = data['summary']

    # Extract the episode information
    episodes = data['_embedded']['episodes']
    episode_list = []

    for episode in episodes:
        episode_number = episode['number']
        episode_title = episode['name']
        episode_airdate = episode['airdate']
        episode_list.append({'Episode Number': episode_number, 'Title': episode_title, 'Airdate': episode_airdate})

    # Print the extracted information
    print("Show Name:", show_name)
    print("Genres:", ', '.join(show_genre))
    print("Summary:", show_summary)
    print("\nEpisode List:")

    for episode in episode_list:
        print("Episode Number:", episode['Episode Number'])
        print("Title:", episode['Title'])
        print("Airdate:", episode['Airdate'])
        print('---')
else:
    print("Failed to download the data. Check the URL or try again later.")
