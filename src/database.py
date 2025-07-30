import os
from dotenv import load_dotenv
import sqlite3

load_dotenv()

DB_CONNECTION_STRING = os.getenv("DB_CONNECTION_STRING")
connection = sqlite3.connect(DB_CONNECTION_STRING)


def store_article(title_id, output, image_filename):
    cursor = connection.cursor()
    cursor.execute('''
        INSERT INTO articles (title_id, output, image_filename)
        VALUES (?, ?, ?)
    ''', (title_id, output, image_filename))
    connection.commit()

    article_id = cursor.lastrowid
    cursor.close()

    return article_id


def store_title(title, suitable, reason):

    cursor = connection.cursor()
    cursor.execute('''
        INSERT INTO titles (title, suitable, reason)
        VALUES (?, ?, ?)
    ''', (title, suitable, reason))
    connection.commit()

    title_id = cursor.lastrowid
    cursor.close()

    return title_id


def title_exists(title):
    cursor = connection.cursor()
    cursor.execute('''
        SELECT COUNT(*) FROM titles WHERE title = ?
    ''', (title,))
    count = cursor.fetchone()[0]
    cursor.close()
    return count > 0

