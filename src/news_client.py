import requests
import os
from dotenv import load_dotenv
import logging

load_dotenv()
logger = logging.getLogger(__name__)

def get_news(search_keyword : str):
    logger.info('Obtaining news from GNews')
    try:
        API_KEY = os.getenv("GNEWS_API_KEY")
        URL = "https://gnews.io/api/v4/search"
        request = requests.get(URL,
                            params={
                                "q" : search_keyword,
                                "lang":"en",
                                "max":10,
                                "apikey":API_KEY
                            },
                            timeout = 15)
        request.raise_for_status()
        return request.json()
    except requests.exceptions.RequestException as e:
        logger.error('Error when obtaining news: %s',e)
        return None

def extract_articles(data):
    articles = data["articles"]
    if not articles:
        logger.warning('No articles were found')
    text = []
    for article in articles:
        text.append(f"{article['title']}. {article['description']}")
    return articles, text
