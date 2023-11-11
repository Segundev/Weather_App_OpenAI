from newsapi import NewsApiClient;
import openai
import json;
import os;
import re;
from bs4 import BeautifulSoup;

# Set your OpenAI API key
api_key = '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'

if os.path.exists('api_data.json'):
    with open('api_data.json', 'r') as file:
        cached_data = json.load(file)
else:
    # Make an API request and save the data
    # Init
    newsapi = NewsApiClient(api_key='61c0091cc9db4a8eb009f0ac5c182aab')
    
    # /v2/everything
    all_articles = newsapi.get_everything(q='weather',
                                      sources='bbc-news',
                                      domains='nimet.gov.ng, guardian.ng, vanguardngr.com, punchng.com, thisdaylive.com, dailytrust.com, channelstv.com, leadership.ng, saharareporters.com, thenationonlineng.net',
                                      from_param='2023-10-07',
                                      to='2023-11-04',
                                      language='en',
                                      sort_by='relevancy',
                                      page=2)
    serialized_data = json.dumps(all_articles)
    # save the file in a json object
    with open('api_data.json', 'w') as file:
        file.write(serialized_data)


# Fetch the "articles" array
articles = cached_data['articles']

# Define a function to clean and format text
def clean_and_format_text(text):
    # Remove HTML tags and entities
    soup = BeautifulSoup(text, 'html.parser')
    clean_text = soup.get_text()
    
    # Remove punctuation and extra whitespace
    clean_text = re.sub(r'[^\w\s]', '', clean_text)
    clean_text = re.sub(r'\s+', ' ', clean_text).strip()
    
    return clean_text

# Clean and format text in each article
for article in articles:
    article['description'] = clean_and_format_text(article['description'])

# Print the articles with formatted text
for article in articles:
    print("Formatted Text:")
    print(article['description'])
    print("\n")
    
