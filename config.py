DB_NAME = "db.sqlite3"

NO_TRANSLATIONS_ERROR = (
    "You have no translations added to your dictionary.\n"
    "Use add parameter to add one."
)


HELP_LINES = (
    "Space - show translation or next text",
    "d - delete current text and translation from dictionary",
    "h - open/close help",
    "q - quit the program",
)


URWID_PALETTE = (
    ("text", "dark blue", ""),
    ("translation", "yellow", ""),
    ("footer", "light gray", ""),
)
