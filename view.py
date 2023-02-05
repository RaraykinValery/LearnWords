import os

import config


def print_element_with_hint(element: str) -> None:
    print(element)
    input(config.HINT_STRING)
    clear_screen()


def clear_screen() -> None:
    os.system("clear" if os.name == "posix" else "cls")
