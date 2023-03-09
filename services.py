from view import urwid_loop


def start_learn_loop() -> None:
    urwid_loop.run()


def greetings() -> None:
    print("WELCOME to LearnWords!\n" "To read help use -h or --help options\n")
