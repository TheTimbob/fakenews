from generate import create_article
from scrape import evaluate_title, get_rss_feed_entries


def main():

    feeds = get_rss_feed_entries()
    if not feeds:
        exit(1)
    
    for feed in feeds:
        title = feed.title if hasattr(feed, 'title') else "Default Article Header"
        suitable, reason = evaluate_title(title)

        print(f"\nsuitable: {suitable}")
        print(f"Reason: {reason}\n")

        if suitable:
            print(f"Creating article for: {title}")
            article = create_article(title)
            print(article)
            exit(0)

    print("No articles created. Exiting.")
    exit(1)


if __name__ == "__main__":
    main()