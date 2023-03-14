import urwid

import pages
import database


def handle_input_keys(key):
    match key:
        case " ":
            if pages.frame.contents["body"][0] == pages.main_page:
                pages.text_translation_widget.show_next()
        case "h":
            if pages.frame.contents["body"][0] != pages.help_page:
                pages.frame.contents["body"] = (pages.help_page, None)
                pages.footer.set_text("")
        case "d":
            if pages.frame.contents["body"][0] == pages.main_page:
                id = pages.text_translation_widget.get_current_unit_id()
                if id:
                    database.delete_text_and_translation_from_db(id)
                    pages.text_translation_widget.show_new_unit()
        case "a":
            if pages.frame.contents["body"][0] != pages.add_text_page:
                pages.frame.contents["body"] = (pages.add_text_page, None)
                pages.footer.set_text(
                    ("footer", "Press esc to close add page"))
        case "enter":
            if pages.frame.contents["body"][0] == pages.add_text_page:
                id = pages.text_translation_widget.get_current_unit_id()
                if not id:
                    pages.text_translation_widget.show_next()
        case "esc":
            if pages.frame.contents["body"][0] != pages.main_page:
                pages.frame.contents["body"] = (pages.main_page, None)
                pages.footer.set_text(("footer", "Press h to open help"))


def handle_sigint(sig, frame):
    raise urwid.ExitMainLoop()
