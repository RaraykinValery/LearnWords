from database import get_random_text_and_translation
import urwid


def show_help(help_panel, help_win):
    help_panel.show()
    while True:
        key = help_win.getch()
        if key == ord("h"):
            help_panel.hide()
            break


def start_learn_loop() -> None:
    def handle(key):
        if key == "q":
            raise urwid.ExitMainLoop()
        if key == " ":
            text, translation = get_random_text_and_translation()
            text_widget.set_text(("text", text))
            translation_widget.set_text(("translation", translation))
        if key == "h":
            if frame.contents["body"][0] != help_page:
                frame.contents["body"] = (help_page, None)
                footer.set_text(get_footer_text("close"))
            else:
                frame.contents["body"] = (main_page, None)
                footer.set_text(get_footer_text("open"))

    text, translation = get_random_text_and_translation()

    palette = [
        ("text", "dark blue", ""),
        ("translation", "yellow", ""),
        ("footer", "light gray", ""),
    ]

    # Main page with text and translation
    text_widget = urwid.Text(("text", text), "center")
    text_filler = urwid.Filler(text_widget, valign="bottom", bottom=1)
    text_padding = urwid.Padding(text_filler, left=2, right=2)

    translation_widget = urwid.Text(("translation", translation), "center")
    translation_filler = urwid.Filler(translation_widget, valign="top")
    translation_padding = urwid.Padding(translation_filler, left=2, right=2)

    main_page = urwid.Pile([text_padding, translation_padding])

    # Help page
    help_texts = [
        "Space - show translation or next text",
        "d - delete current text and translation from dictionary",
        "h - open/close help",
        "q - quit the program",
    ]

    help_pile = urwid.Pile([])

    for txt in help_texts:
        help_pile.contents.append((urwid.Text(txt), help_pile.options()))

    help_pile_filler = urwid.Filler(help_pile, top=2, bottom=2)
    help_pile_filler_padding = urwid.Padding(
        help_pile_filler, align="center", left=2, right=2
    )

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
    def get_footer_text(action: str) -> tuple[str, str]:
        return ("footer", "Press h to {action} help".format(action=action))

    footer = urwid.Text(get_footer_text("open"), "left")

    frame = urwid.Frame(main_page, footer=footer, focus_part="footer")

    loop = urwid.MainLoop(frame, palette, unhandled_input=handle)
    loop.run()


def greetings(args) -> None:
    print("WELCOME to LearnWords!\n" "To read help use -h or --help options\n")
