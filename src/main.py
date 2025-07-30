from database import store_title, title_exists, store_article
from generate import create_article, create_image, download_image
from scrape import evaluate_title, get_rss_feed_entries


def main():

    feeds = get_rss_feed_entries()
    if not feeds:
        exit(1)

    for feed in feeds:
        title = feed.title if hasattr(feed, 'title') else "Default Article Header"

        if title_exists(title):
            print(f"Title '{title}' already exists in the database. Skipping.")
            continue

        suitable, reason = evaluate_title(title)
        title_id = store_title(title, suitable, reason)

        print(f"\nEvaluating title: {title}")
        print(f"Suitable: {suitable}")
        print(f"Reason: {reason}\n")

        if suitable:
            article = create_article(title)
            print(article)

            image_url = create_image(title)
            image_filename = f"{title[:25].lower().replace(' ', '_')}.png"
            download_image(image_url, image_filename)

            store_article(title_id, article, image_filename)
            exit(0)

    print("No articles created. Exiting.")
    exit(1)


if __name__ == "__main__":
    main()