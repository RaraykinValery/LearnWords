import urwid

from database import (
    get_random_text_and_translation,
    insert_text_and_translation_to_db,
    DictUnit,
)
from exceptions import NoUnitsInDictionary
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
                ("success", config.SAVING_SUCCESS_MESSAGE))
            self.__clear__text_widgets()
            super().set_focus(self.__text_edit_lined)


class TextTranslationWidget(urwid.Pile):
    def __init__(self) -> None:
        self.__current_dict_unit: DictUnit | None = None

        self.__text_widget = urwid.Text(("text", ""), align="center")
        self.__translation_widget = urwid.Text(
            ("translation", ""), align="center")

        self.__show_new_unit = True
        self.__need_init_unit = True

        self.show_next()

        super().__init__(
            [self.__text_widget, urwid.Divider(), self.__translation_widget])

    def __set_unit(self) -> None:
        self.__current_dict_unit = get_random_text_and_translation(
            self.__current_dict_unit
        )

    def __show_text(self, text: str, attr: str = "text") -> None:
        self.__text_widget.set_text((attr, text))

    def __show_translation(self, translation: str, attr: str = "translation") -> None:
        self.__translation_widget.set_text((attr, translation))

    def __clear_widgets_text(self) -> None:
        self.__text_widget.set_text(("text", ""))
        self.__translation_widget.set_text(("translation", ""))

    def get_current_unit_id(self) -> int | None:
        if self.__current_dict_unit:
            return self.__current_dict_unit.id
        else:
            return None

    def show_next(self) -> None:
        if self.__show_new_unit:
            self.__clear_widgets_text()
            try:
                self.__set_unit()
            except NoUnitsInDictionary:
                self.__show_text(config.NO_UNITS_ERROR, "")
                self.__show_new_unit = True
            else:
                self.__show_text(self.__current_dict_unit.text)
                self.__show_new_unit = False
                if self.__need_init_unit:
                    self.__need_init_unit = False
        else:
            self.__show_translation(self.__current_dict_unit.translation)
            self.__show_new_unit = True

    def show_new_unit(self) -> None:
        self.__show_new_unit = True
        self.__current_dict_unit = None
        self.show_next()
