import urwid

from database import get_random_text_and_translation, insert_text_and_translation_to_db


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
            if super().get_focus() == self.text_edit_lined:
                super().set_focus(self.translation_edit_lined)
            else:
                super().set_focus(self.text_edit_lined)
        if key == "enter":
            if (
                self.text_edit.text.strip() == ""
                or self.translation_edit.text.strip() == ""
            ):
                self.information_field.set_text(
                    (
                        "error",
                        "To save, you need to fill in both the text and translation fields",
                    )
                )
            else:
                text = self.text_edit.text.strip()
                translation = self.translation_edit.text.strip()
                insert_text_and_translation_to_db(text, translation)
                self.information_field.set_text(
                    ("success", "Saved successfully!"))
                self.text_edit.set_edit_text("")
                self.translation_edit.set_edit_text("")
                super().set_focus(self.text_edit_lined)
        else:
            return super().keypress(size, key)


class TextTranslationWidget(urwid.Pile):
    def __init__(self) -> None:
        self.text_id: int
        self.text: str
        self.translation: str

        self.text_widget = urwid.Text(("text", ""), align="center")
        self.translation_widget = urwid.Text(
            ("translation", ""), align="center")

        self._translation_showed = False

        self._set_text_translation()
        self._show_text(self.text)

        super().__init__(
            [self.text_widget, urwid.Divider(), self.translation_widget])

    def _set_text_translation(self, id=None) -> None:
        self.text_id, self.text, self.translation = get_random_text_and_translation(
            id)

    def _show_text(self, text: str) -> None:
        self.text_widget.set_text(("text", text))

    def _show_translation(self, translation: str) -> None:
        self.translation_widget.set_text(("translation", translation))

    def _clear_widgets_text(self):
        self.text_widget.set_text(("text", ""))
        self.translation_widget.set_text(("translation", ""))

    def show_next(self) -> None:
        if self._translation_showed:
            self._set_text_translation(self.text_id)
            self._clear_widgets_text()
            self._show_text(self.text)
            self._translation_showed = False
        else:
            self._show_translation(self.translation)
            self._translation_showed = True

    def show_new_text(self) -> None:
        self._set_text_translation()
        self._clear_widgets_text()
        self._show_text(self.text)
        self._translation_showed = False
