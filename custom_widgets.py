from typing import Optional
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
        self.text_edit = urwid.Edit()
        self.text_edit_lined = urwid.LineBox(
            self.text_edit, title="Text", title_attr="text"
        )
        self.translation_edit = urwid.Edit()
        self.translation_edit_lined = urwid.LineBox(
            self.translation_edit, title="Translation", title_attr="translation"
        )
        self.information_field = urwid.Text("", "center")
        self.blank = urwid.Divider()

        super().__init__(
            [
                self.text_edit_lined,
                self.blank,
                self.translation_edit_lined,
                self.blank,
                self.information_field,
            ]
        )

    def keypress(self, size, key):
        if key == "tab":
            self._toggle_focus()
        if key == "enter":
            self._add_unit_to_dictionary()
            return super().keypress(size, key)
        if key == "esc":
            self._clear_text_widgets()
            self.information_field.set_text("")
            return super().keypress(size, key)
        else:
            return super().keypress(size, key)

    def _clear_text_widgets(self) -> None:
        self.text_edit.set_edit_text("")
        self.translation_edit.set_edit_text("")

    def _toggle_focus(self) -> None:
        if super().get_focus() == self.text_edit_lined:
            super().set_focus(self.translation_edit_lined)
        else:
            super().set_focus(self.text_edit_lined)

    def _add_unit_to_dictionary(self) -> None:
        if (
            self.text_edit.text.strip() == ""
            or self.translation_edit.text.strip() == ""
        ):
            self.information_field.set_text(
                ("error", config.EMPTY_REQUIRED_FIELDS_ERROR)
            )
        else:
            text = self.text_edit.text.strip()
            translation = self.translation_edit.text.strip()
            insert_text_and_translation_to_db(text, translation)
            self.information_field.set_text(
                ("success", config.SAVING_SUCCESS_MESSAGE))
            self._clear_text_widgets()
            super().set_focus(self.text_edit_lined)


class TextTranslationWidget(urwid.Pile):
    def __init__(self) -> None:
        self._current_dict_unit: Optional[DictUnit] = None

        self._text_widget = urwid.Text(("text", ""), align="center")
        self._translation_widget = urwid.Text(
            ("translation", ""), align="center")

        self._show_new_unit = True
        self._need_init_unit = True

        self.show_next()

        super().__init__(
            [self._text_widget, urwid.Divider(), self._translation_widget])

    def _set_unit(self) -> None:
        self._current_dict_unit = get_random_text_and_translation(
            self._current_dict_unit
        )

    def _show_text(self, text: str, attr: str = "text") -> None:
        self._text_widget.set_text((attr, text))

    def _show_translation(self, translation: str, attr: str = "translation") -> None:
        self._translation_widget.set_text((attr, translation))

    def _clear_widgets_text(self) -> None:
        self._text_widget.set_text(("text", ""))
        self._translation_widget.set_text(("translation", ""))

    def get_current_unit_id(self) -> Optional[int]:
        if self._current_dict_unit:
            return self._current_dict_unit.id
        else:
            return None

    def show_next(self) -> None:
        if self._show_new_unit:
            self._clear_widgets_text()
            try:
                self._set_unit()
            except NoUnitsInDictionary:
                self._show_text(config.NO_UNITS_ERROR, "")
                self._show_new_unit = True
            else:
                self._show_text(self._current_dict_unit.text)
                self._show_new_unit = False
                if self._need_init_unit:
                    self._need_init_unit = False
        else:
            self._show_translation(self._current_dict_unit.translation)
            self._show_new_unit = True

    def show_new_unit(self) -> None:
        self._show_new_unit = True
        self._current_dict_unit = None
        self.show_next()
