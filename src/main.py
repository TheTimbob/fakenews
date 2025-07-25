from generate import create_article
from scrape import get_rss_feed_entries


def main():

    feeds = get_rss_feed_entries()
    if not feeds:
        exit(1)
    
    for feed in feeds:
        article_header = feed.title if hasattr(feed, 'title') else "Default Article Header"
        generate = input(f"Generate Article (Y/N)? Article Title: {article_header}\n")

        if generate.lower() in ['y', 'yes']:
            print(f"Creating article for: {article_header}")
            article = create_article(article_header)
            print(article)
            exit(0)

    print("No articles created. Exiting.")
    exit(1)


if __name__ == "__main__":
    main()