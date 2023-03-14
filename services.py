import signal

import urwid

import config
from handlers import handle_sigint, handle_input_keys
import pages


def start_learn_loop() -> None:
    signal.signal(signal.SIGINT, handle_sigint)

    urwid.MainLoop(
        pages.frame, config.URWID_PALETTE, unhandled_input=handle_input_keys
    ).run()


def greetings() -> None:
    print(config.GREETINGS_MESSAGE)
