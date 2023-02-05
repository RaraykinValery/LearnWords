import sqlite3
import os

import config


db_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "db.sqlite3")


def create_table_if_not_exists() -> None:
    with sqlite3.connect(db_path) as connection:
        connection.execute(
            """
            CREATE TABLE IF NOT EXISTS dictionary(
                id integer PRIMARY KEY,
                primary_text varchar(255) NOT NULL UNIQUE,
                translation varchar(255) NOT NULL
            )
            """
        )


def insert_text_and_translation_to_db(text: str, translation: str) -> None:
    try:
        with sqlite3.connect(db_path) as connection:
            connection.execute(
                "INSERT INTO dictionary (primary_text, translation) VALUES(?, ?)",
                [text, translation],
            )
    except sqlite3.IntegrityError as err:
        print(f"Couldn't add translation.\nError: {err}")


def get_random_text_and_translation() -> tuple[str, str]:
    try:
        with sqlite3.connect(db_path) as connection:
            row = connection.execute(
                "SELECT primary_text, translation FROM dictionary ORDER BY RANDOM() LIMIT 1"
            ).fetchone()
    except sqlite3.IntegrityError as err:
        print(f"Couldn't add translation.\nError: {err}")

    if row is None:
        print(config.NO_TRANSLATIONS_ERROR)
        exit()

    return row