import signal

import urwid

from view import urwid_loop
import config


def start_learn_loop() -> None:
    signal.signal(signal.SIGINT, handle_sigint)

    urwid_loop.run()


def handle_sigint(sig, frame):
    raise urwid.ExitMainLoop()


def greetings() -> None:
    print(config.GREETINGS_MESSAGE)
