import config
from view import clear_screen, print_element_with_hint
from database import get_random_text_and_translation


def start_learn_loop() -> None:
    clear_screen()
    while True:
        text, translation = get_random_text_and_translation()
        print_element_with_hint(config.TEXT_STRING.format(text=text))
        print_element_with_hint(
            config.TRANSLATION_STRING.format(translation=translation)
        )


def handler(signum, frame) -> None:
    clear_screen()
    print("See you soon!")
    exit()


def greetings(args) -> None:
    print("WELCOME to LearnWords!\n" "To read help use -h or --help options\n")
