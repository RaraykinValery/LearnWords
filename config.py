DB_NAME = "db.sqlite3"

GREETINGS_MESSAGE = "WELCOME to LearnWords!\nTo read help use -h or --help options\n"

NO_UNITS_ERROR = (
    "No translations have been added to your dictionary.\n"
    "To add one, press 'a' or use 'LearnWords add' command."
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

EMPTY_REQUIRED_FIELDS_ERROR = (
    "To save, you need to fill in both the text and translation fields"
)

SAVING_SUCCESS_MESSAGE = "Saved successfully!"
