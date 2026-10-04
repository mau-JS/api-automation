import requests
import os
from dotenv import load_dotenv
import logging

load_dotenv()
logger = logging.getLogger(__name__)

def sentiment_analysis(input_text: list[str]) -> list[dict[int, float]]:
    logger.info('Running sentiment analysis on list')
    API_KEY = os.getenv("NINJAS_API_KEY")
    URL = "https://api.api-ninjas.com/v1/sentiment"
    sentiment_scores = []
    for index,text in enumerate(input_text):
        try:
            request = requests.get(URL,
                                params={
                                    "text":text
                                    },
                                    headers={
                                        "X-Api-Key":API_KEY
                                        },
                                    timeout = 15
                                    )
            request.raise_for_status()
            sentiment_scores.append({index:request.json()['score']})
        except requests.exceptions.RequestException as e:
            logger.error("Error when obtaining sentiment analysis: %s ",e)
    return sentiment_scores

def extract_positive_scores(rating_list):
    logger.info("Extracting positive scores indexes")
    positive_scores = {}

    for i in rating_list:
        for index, score in i.items():
            if score >= 0.5:
                positive_scores[index] = score

    return positive_scores

def obtain_best_article(positive_scores):
    logger.info("Obtaining article with most positive sentiment")
    if not positive_scores:
        return None
    maximum = float("-inf")
    for key,value in positive_scores.items():
        if value > maximum:
            maximum = value
            best_article_index = key
    return best_article_index
