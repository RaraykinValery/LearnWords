DB_NAME = "db.sqlite3"

NO_TRANSLATIONS_ERROR = (
    "You have no translations added to your dictionary.\n"
    "Use add parameter to add one."
)


HELP_LINES = (
    "Space - show translation or next text",
    "d - delete current text and translation from dictionary",
    "esc - back to main page",
    "a - open form for adding new text and translation",
    "Enter (in add page) - save text and translation to dictionary",
    "h - open help",
    "ctrl-c - quit the program",
)


URWID_PALETTE = (
    ("text", "dark blue", ""),
    ("translation", "yellow", ""),
    ("footer", "light gray", ""),
    ("error", "dark red", ""),
    ("success", "dark green", ""),
)
