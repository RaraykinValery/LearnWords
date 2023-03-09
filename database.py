import sqlite3
import os
from typing import NamedTuple

from exceptions import NoUnitsInDictionary


db_path = os.path.join(os.path.dirname(
    os.path.realpath(__file__)), "db.sqlite3")

conn = sqlite3.connect(db_path)
cursor = conn.cursor()


class DictUnit(NamedTuple):
    id: int
    text: str
    translation: str


def insert_text_and_translation_to_db(text: str, translation: str) -> None:
    params = (text, translation)
    cursor.execute(
        "INSERT INTO dictionary (primary_text, translation) VALUES(?, ?)", params
    )
    conn.commit()


def delete_text_and_translation_from_db(id: int) -> None:
    params = (id,)
    cursor.execute("DELETE FROM dictionary WHERE id = ?", params)
    conn.commit()


def get_random_text_and_translation(current_dict_unit: DictUnit | None) -> DictUnit:
    num_rows = cursor.execute("SELECT COUNT(*) FROM dictionary").fetchone()[0]

    if num_rows == 0:
        raise NoUnitsInDictionary

    if current_dict_unit:
        if num_rows == 1:
            return current_dict_unit
        params = (current_dict_unit.id,)
        row = cursor.execute(
            "SELECT id, primary_text, translation "
            "FROM dictionary WHERE id != ? ORDER BY RANDOM() LIMIT 1",
            params,
        ).fetchone()
    else:
        row = cursor.execute(
            "SELECT id, primary_text, translation FROM dictionary ORDER BY RANDOM() LIMIT 1"
        ).fetchone()

    return DictUnit(*row)


def _init_db() -> None:
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS dictionary(
            id integer PRIMARY KEY,
            primary_text varchar(255) NOT NULL,
            translation varchar(255) NOT NULL
        )
        """
    )
    conn.commit()


def check_db_exists() -> None:
    cursor.execute(
        "SELECT name FROM sqlite_master " "WHERE type='table' AND name='dictionary'"
    )
    table_exists = cursor.fetchall()
    if table_exists:
        return
    _init_db()


check_db_exists()
