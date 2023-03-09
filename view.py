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
    if key == "enter":
        if frame.contents["body"][0] == add_text_page:
            id = text_translation_widget.get_current_unit_id()
            if not id:
                text_translation_widget.show_next()
    if key == "esc":
        if frame.contents["body"][0] != main_page:
            frame.contents["body"] = (main_page, None)
            footer.set_text(("footer", "Press h to open help"))


# Main page with text and translation
text_translation_widget = TextTranslationWidget()
main_page = urwid.Filler(text_translation_widget)

# Help page
help_pile = urwid.Pile([])
main_pile = urwid.Pile([])

for binding in config.HELP_LINES:
    key = urwid.Text(("keybinding", binding[0]), "right")
    descr = urwid.Text(("", binding[1]))
    column = urwid.Columns(
        [("weight", 1, key), ("weight", 3, descr)], dividechars=3)
    main_pile.contents.append((column, main_pile.options()))
    main_pile.contents.append((urwid.Divider(), main_pile.options()))

help_page = urwid.Filler(
    urwid.Padding(main_pile, width=("relative", 60),
                  align="center", min_width=70)
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

urwid_loop = urwid.MainLoop(
    frame, config.URWID_PALETTE, unhandled_input=handle_input)
