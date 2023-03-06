from database import get_random_text_and_translation
from config import HELP_LINES, URWID_PALETTE
import urwid


def start_learn_loop() -> None:

    def handle_input(key):
        if key == "q":
            raise urwid.ExitMainLoop()
        if key == " ":
            main_page.show_next()
        if key == "h":
            if frame.contents["body"][0] != help_page:
                frame.contents["body"] = (help_page, None)
                footer.set_text(get_footer_text("close"))
            else:
                frame.contents["body"] = (main_page, None)
                footer.set_text(get_footer_text("open"))
        if key == "j":
            footer.set_text(str(frame.focus))

    def get_footer_text(action: str) -> tuple[str, str]:
        return ("footer", "Press h to {action} help".format(action=action))

    # Main page with text and translation
    class TextTranslationWidget(urwid.Filler):
        def __init__(self) -> None:
            self.text: str
            self.translation: str

            self.translation_showed = False

            self.text_widget = urwid.Text(("text", ""), align="center")
            self.translation_widget = urwid.Text(
                ("translation", ""), align="center")

            self._set_text_translation()
            self._show_text(self.text)

            super().__init__(
                urwid.Pile([self.text_widget, urwid.Divider(),
                           self.translation_widget])
            )

        def _set_text_translation(self) -> None:
            self.text, self.translation = get_random_text_and_translation()

        def _show_text(self, text: str) -> None:
            self.text_widget.set_text(("text", text))

        def _show_translation(self, translation: str) -> None:
            self.translation_widget.set_text(("translation", translation))

        def show_next(self) -> None:
            if self.translation_showed:
                self.text_widget.set_text(("text", ""))
                self.translation_widget.set_text(("translation", ""))
                self._set_text_translation()
                self._show_text(self.text)
                self.translation_showed = False
            else:
                self._show_translation(self.translation)
                self.translation_showed = True

    main_page = TextTranslationWidget()

    # Help page
    help_pile = urwid.Pile([])

    for txt in HELP_LINES:
        help_pile.contents.append(
            (
                urwid.Text(txt),
                help_pile.options(),
            )
        )

    help_pile_filler = urwid.Filler(urwid.Padding(help_pile, "center", "pack"))
    help_pile_filler_padding = help_pile_filler

    overlay_bottom_w = urwid.SolidFill()

    help_page = urwid.Overlay(
        top_w=help_pile_filler_padding,
        bottom_w=overlay_bottom_w,
        align="center",
        valign="middle",
        height=("relative", 30),
        width=("relative", 70),
    )

    # Main frame
    footer = urwid.Text(get_footer_text("open"), "left")

    frame = urwid.Frame(main_page, footer=footer)

    loop = urwid.MainLoop(frame, URWID_PALETTE, unhandled_input=handle_input)
    loop.run()


def greetings(args) -> None:
    print("WELCOME to LearnWords!\n" "To read help use -h or --help options\n")
