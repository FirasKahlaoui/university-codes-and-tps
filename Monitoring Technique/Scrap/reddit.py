import requests
import csv
from datetime import datetime

# Define competitors including new ones: weeFARM, Bakourat, Palmotek, SmartFarm
competitors = [
    "John Deere", "Case IH", "Claas", "Kubota", "AG Leader", "Trimble",
    "Bayer CropScience", "SmartFarm Bakorat", "weeFARM", "Bakourat",
    "Palmotek", "SmartFarm"
]

# Function to fetch mentions from Reddit


def fetch_reddit_mentions(competitors):
    url = "https://www.reddit.com/r/all/search.json"
    mentions = []

    for competitor in competitors:
        params = {'q': competitor, 'limit': 10}
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url, headers=headers, params=params)

        if response.status_code == 200:
            data = response.json()
            for post in data['data']['children']:
                mention_time = datetime.utcfromtimestamp(
                    post['data']['created_utc'])
                mentions.append({
                    'competitor': competitor,
                    'mention_time': mention_time,
                    'platform': 'Reddit',
                    'title': post['data']['title'],
                    'url': f"https://www.reddit.com{post['data']['permalink']}"
                })
    return mentions

# Function to fetch mentions from NewsAPI


def fetch_news_mentions(competitors):
    api_key = "YOUR_NEWSAPI_KEY"
    url = "https://newsapi.org/v2/everything"
    mentions = []

    for competitor in competitors:
        params = {'q': competitor, 'apiKey': api_key}
        response = requests.get(url, params=params)

        if response.status_code == 200:
            data = response.json()
            for article in data['articles']:
                mention_time = datetime.strptime(
                    article['publishedAt'], '%Y-%m-%dT%H:%M:%S%z')
                mentions.append({
                    'competitor': competitor,
                    'mention_time': mention_time,
                    'platform': 'NewsAPI',
                    'title': article['title'],
                    'url': article['url']
                })
    return mentions


def write_to_csv(mentions, filename='competitor_mentions.csv'):
    keys = mentions[0].keys()
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=keys)
        writer.writeheader()
        writer.writerows(mentions)


# Fetch data from both Reddit and NewsAPI
reddit_mentions = fetch_reddit_mentions(competitors)
news_mentions = fetch_news_mentions(competitors)

# Combine the results
all_mentions = reddit_mentions + news_mentions

# Write to CSV
write_to_csv(all_mentions)

print(f"Data saved to 'competitor_mentions.csv'.")
