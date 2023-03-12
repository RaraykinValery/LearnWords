import urwid

import config
import custom_widgets

# Main page with text and translation
text_translation_widget = custom_widgets.TextTranslationWidget()
main_page = urwid.Filler(text_translation_widget)

# Help page
help_pile = urwid.Pile([])
main_pile = urwid.Pile([])

for binding in config.HELP_LINES:
    key = urwid.Text(("keybinding", binding[0]))
    descr = urwid.Text(("", binding[1]))
    column = urwid.Columns(
        [("weight", 1, key), ("weight", 5, descr)], dividechars=3)
    main_pile.contents.append((column, main_pile.options()))
    main_pile.contents.append((urwid.Divider(), main_pile.options()))

help_page = urwid.Filler(
    urwid.Padding(main_pile, width=("relative", 40),
                  align="center", min_width=50)
)

# Add text page
add_text_translation_form = custom_widgets.AddTextTranslationForm()
add_text_page = urwid.Filler(
    urwid.Padding(add_text_translation_form, width=(
        "relative", 50), align="center")
)

# Main frame
header = urwid.Text("", "left")
footer = urwid.Text(("footer", "Press h to open help"))

frame = urwid.Frame(main_page, footer=footer, header=header)
