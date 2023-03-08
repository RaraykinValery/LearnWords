import sqlite3
import os

import config


db_path = os.path.join(os.path.dirname(
    os.path.realpath(__file__)), "db.sqlite3")

conn = sqlite3.connect(db_path)
cursor = conn.cursor()


def insert_text_and_translation_to_db(text: str, translation: str) -> None:
    cursor.execute(
        "INSERT INTO dictionary (primary_text, translation) VALUES(?, ?)",
        [text, translation],
    )


def delete_text_and_translation_from_db(id: int) -> None:
    params = (id,)
    cursor.execute("DELETE FROM dictionary WHERE id = ?", params)


def get_random_text_and_translation(
    current_text_id: int | None = None,
) -> tuple[int, str, str]:
    if current_text_id:
        params = (current_text_id,)
        row = cursor.execute(
            "SELECT id, primary_text, translation "
            "FROM dictionary WHERE id != ? ORDER BY RANDOM() LIMIT 1",
            params,
        ).fetchone()
    else:
        row = cursor.execute(
            "SELECT id, primary_text, translation FROM dictionary ORDER BY RANDOM() LIMIT 1"
        ).fetchone()

    if row is None:
        print(config.NO_TRANSLATIONS_ERROR)
        exit()

    return row


def _init_db() -> None:
    cursor.executescript(
        """
        CREATE TABLE IF NOT EXISTS dictionary(
            id integer PRIMARY KEY,
            primary_text varchar(255) NOT NULL UNIQUE,
            translation varchar(255) NOT NULL
        )
        """
    )
    conn.commit()


def check_db_exists() -> None:
    cursor.execute(
        "SELECT name FROM sqlite_master "
        "WHERE type='table' AND name='dictionary'"
    )
    table_exists = cursor.fetchall()
    if table_exists:
        return
    _init_db()


check_db_exists()
