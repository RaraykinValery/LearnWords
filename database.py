import sqlite3
import os

import config
from exceptions import (
    CanNotCreateDatabase,
    CanNotDeleteTextAndTranslation,
    CanNotAddTextAndTranslation,
    CanNotGetTextAndTranslation,
)


db_path = os.path.join(os.path.dirname(
    os.path.realpath(__file__)), "db.sqlite3")


def create_table_if_not_exists() -> None:
    try:
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
    except Exception:
        raise CanNotCreateDatabase


def insert_text_and_translation_to_db(text: str, translation: str) -> None:
    try:
        with sqlite3.connect(db_path) as connection:
            connection.execute(
                "INSERT INTO dictionary (primary_text, translation) VALUES(?, ?)",
                [text, translation],
            )
    except sqlite3.IntegrityError:
        raise CanNotAddTextAndTranslation


def delete_text_and_translation_from_db(id: int) -> None:
    try:
        with sqlite3.connect(db_path) as connection:
            params = (id,)
            connection.execute("DELETE FROM dictionary WHERE id = ?", params)
    except sqlite3.IntegrityError:
        raise CanNotDeleteTextAndTranslation


def get_random_text_and_translation(
    current_text_id: int | None = None,
) -> tuple[int, str, str]:
    try:
        with sqlite3.connect(db_path) as connection:
            if current_text_id:
                params = (current_text_id,)
                row = connection.execute(
                    "SELECT id, primary_text, translation FROM dictionary WHERE id != ? ORDER BY RANDOM() LIMIT 1",
                    params
                ).fetchone()
            else:
                row = connection.execute(
                    "SELECT id, primary_text, translation FROM dictionary ORDER BY RANDOM() LIMIT 1"
                ).fetchone()
    except sqlite3.IntegrityError:
        raise CanNotGetTextAndTranslation

    if row is None:
        print(config.NO_TRANSLATIONS_ERROR)
        exit()

    return row
