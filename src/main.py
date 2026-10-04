from news_service import get_news, extract_articles
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def main():
    logger.info("Automation code")
    favorite_category = "technology"
    data = get_news(favorite_category)
    if data is None:
        logger.error("Could not retrieve news")
        return
    articles,text = extract_articles(data)
    logger.info("Retrieved %s articles",len(articles))

if __name__ == "__main__":
    main()