import sqlite3

import config
from view import clear_screen, print_element_with_hint


def start_learn_loop() -> None:
    clear_screen()
    while True:
        text, translation = get_random_text_and_translation()
        print_element_with_hint(config.TEXT_STRING.format(text=text))
        print_element_with_hint(
            config.TRANSLATION_STRING.format(translation=translation)
        )


def create_table_if_not_exists() -> None:
    with sqlite3.connect("db.sqlite3") as connection:
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
        with sqlite3.connect("db.sqlite3") as connection:
            connection.execute(
                "INSERT INTO dictionary (primary_text, translation) VALUES(?, ?)",
                [text, translation],
            )
    except sqlite3.IntegrityError as err:
        print(f"Couldn't add translation.\nError: {err}")


def get_random_text_and_translation() -> tuple[str, str]:
    try:
        with sqlite3.connect("db.sqlite3") as connection:
            row = connection.execute(
                "SELECT primary_text, translation FROM dictionary ORDER BY RANDOM() LIMIT 1"
            ).fetchone()
    except sqlite3.IntegrityError as err:
        print(f"Couldn't add translation.\nError: {err}")

    if row is None:
        print(config.NO_TRANSLATIONS_ERROR)
        exit()

    return row


def handler(signum, frame) -> None:
    clear_screen()
    print("See you soon!")
    exit()


def greetings(args) -> None:
    print("WELCOME to LearnWords!\n" "To read help use -h or --help options\n")
