from news_client import get_news, extract_articles
from sentiment_service import sentiment_analysis, extract_positive_scores, obtain_best_article
from user_repository import get_user_data
from email_service import send_mail
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def main():
    logger.info("Automation code")
    user_id = input("Please insert the user_id you would like to send positive news: ")
    try:
        user_dictionary = get_user_data(user_id)
        user_email = user_dictionary["email"]
        favorite_category = user_dictionary["category"]
        user_name = user_dictionary["name"]
    except ValueError as e:
        logger.error("Error: %s",e)
        return
    data = get_news(favorite_category)
    if data is None:
        logger.error("Could not retrieve news")
        return
    articles, text = extract_articles(data)
    logger.info("Retrieved %s articles",len(articles))
    rating_list = sentiment_analysis(text)
    positive_scores = extract_positive_scores(rating_list)
    best_index = obtain_best_article(positive_scores)
    if best_index is not None:
        best_article = articles[best_index]
        logger.info("Best article index: %s", best_index)
        logger.info("Rating List: %s",rating_list)
        logger.info("Positive Scores: %s",positive_scores)
        subject = f"Good News for you in {favorite_category}, {user_name}!"
        try:
            send_mail(
                address=user_email,
                subject=subject,
                body = (
                    f"Hi {user_name}! Here is some good news that might interest you:\n\n"
                    f"{best_article['title']}\n\n"
                    f"Read full article: {best_article['url']}")
            )
        except Exception as e:
            logger.error("Failed to send email: %s", e)
    else:
        logger.warning("Could not find a sufficiently positive article within the list")
        return

if __name__ == "__main__":
    main()