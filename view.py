import urwid

import config
from database import (
    delete_text_and_translation_from_db,
)
from custom_widgets import AddTextTranslationForm, TextTranslationWidget


def handle_input(key):
    if key == " ":
        if frame.contents["body"][0] == main_page:
            text_translation_widget.show_next()
    if key == "h":
        if frame.contents["body"][0] != help_page:
            frame.contents["body"] = (help_page, None)
            footer.set_text("")
    if key == "d":
        if frame.contents["body"][0] == main_page:
            id = text_translation_widget.get_current_unit_id()
            if id:
                delete_text_and_translation_from_db(id)
                text_translation_widget.show_new_unit()
    if key == "a":
        if frame.contents["body"][0] != add_text_page:
            frame.contents["body"] = (add_text_page, None)
            footer.set_text(("footer", "Press esc to close add page"))
    if key == "esc":
        if frame.contents["body"][0] != main_page:
            frame.contents["body"] = (main_page, None)
            footer.set_text(("footer", "Press h to open help"))


# Main page with text and translation
text_translation_widget = TextTranslationWidget()
main_page = urwid.Filler(text_translation_widget)

# Help page
help_pile = urwid.Pile([])

for txt in config.HELP_LINES:
    help_pile.contents.append(
        (
            urwid.Text(txt + "\n"),
            help_pile.options(),
        )
    )

help_page = urwid.Filler(
    urwid.Padding(help_pile, align="center", width=("relative", 60))
)

# Add text page
add_text_translation_form = AddTextTranslationForm()
add_text_page = urwid.Filler(
    urwid.Padding(add_text_translation_form, width=(
        "relative", 50), align="center")
)

# Main frame
header = urwid.Text("", "left")
footer = urwid.Text(("footer", "Press h to open help"))

frame = urwid.Frame(main_page, footer=footer, header=header)

urwid_loop = urwid.MainLoop(frame, config.URWID_PALETTE, unhandled_input=handle_input)
