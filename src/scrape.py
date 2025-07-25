import feedparser
from dotenv import load_dotenv
import os

load_dotenv()

FEED_URL = os.getenv("RSS_FEED_URL")


def get_rss_feed():
    if not FEED_URL:
        print("Error: RSS_FEED_URL not set in environment variables.")
        return None

    return feedparser.parse(FEED_URL)


def get_rss_feed_entries():
    rss_feed = get_rss_feed()
    if not rss_feed:
        print("Error: Could not retrieve RSS feed.")
        return None

    return rss_feed.entries


def default_article_header():
    return "Ghislaine Maxwell's attorney says she is 'not suicidal' and 'not going to kill herself' as she awaits sentencing."
