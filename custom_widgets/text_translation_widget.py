import urwid

from database import (
    get_random_text_and_translation,
    DictUnit,
)
from exceptions import NoUnitsInDictionary
import config


class TextTranslationWidget(urwid.Pile):
    def __init__(self) -> None:
        self.__current_dict_unit: DictUnit | None = None

        self.__text_widget = urwid.Text(("text", ""), align="center")
        self.__translation_widget = urwid.Text(
            ("translation", ""), align="center"
        )

        self.__show_new_unit = True
        self.__need_init_unit = True

        self.show_next()

        super().__init__(
            [self.__text_widget, urwid.Divider(), self.__translation_widget]
        )

    def __set_unit(self) -> None:
        self.__current_dict_unit = get_random_text_and_translation(
            self.__current_dict_unit
        )

    def __show_text(self, text: str, attr: str = "text") -> None:
        self.__text_widget.set_text((attr, text))

    def __show_translation(
        self, translation: str, attr: str = "translation"
    ) -> None:
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
