import urwid

from database import (
    insert_text_and_translation_to_db,
)
import config


class AddTextTranslationForm(urwid.Pile):
    def __init__(self) -> None:
        self.__text_edit = urwid.Edit()
        self.__text_edit_lined = urwid.LineBox(
            self.__text_edit, title="Text", title_attr="text"
        )
        self.__translation_edit = urwid.Edit()
        self.__translation_edit_lined = urwid.LineBox(
            self.__translation_edit, title="Translation", title_attr="translation"
        )
        self.__information_field = urwid.Text("", "center")
        self.__blank = urwid.Divider()

        super().__init__(
            [
                self.__text_edit_lined,
                self.__blank,
                self.__translation_edit_lined,
                self.__blank,
                self.__information_field,
            ]
        )

    def keypress(self, size, key):
        if key == "tab":
            self.__toggle_focus()
        if key == "enter":
            self.__add_unit_to_dictionary()
            return super().keypress(size, key)
        if key == "esc":
            self.__clear__text_widgets()
            self.__information_field.set_text("")
            return super().keypress(size, key)
        else:
            return super().keypress(size, key)

    def __clear__text_widgets(self) -> None:
        self.__text_edit.set_edit_text("")
        self.__translation_edit.set_edit_text("")

    def __toggle_focus(self) -> None:
        if super().get_focus() == self.__text_edit_lined:
            super().set_focus(self.__translation_edit_lined)
        else:
            super().set_focus(self.__text_edit_lined)

    def __add_unit_to_dictionary(self) -> None:
        if (
            self.__text_edit.text.strip() == ""
            or self.__translation_edit.text.strip() == ""
        ):
            self.__information_field.set_text(
                ("error", config.EMPTY_REQUIRED_FIELDS_ERROR)
            )
        else:
            text = self.__text_edit.text.strip()
            translation = self.__translation_edit.text.strip()
            insert_text_and_translation_to_db(text, translation)
            self.__information_field.set_text(
                ("success", config.SAVING_SUCCESS_MESSAGE)
            )
            self.__clear__text_widgets()
            super().set_focus(self.__text_edit_lined)
