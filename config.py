DB_NAME = "db.sqlite3"

GREETINGS_MESSAGE = (
    "WELCOME to LearnWords!\nTo read help use -h or --help options\n"
)

NO_UNITS_ERROR = (
    "No translations have been added to your dictionary.\n"
    "To add one, press 'a' or use 'LearnWords add' command."
)

HELP_LINES = (
    ("a", "open form for adding new text and translation"),
    ("d", "delete current text and translation from dictionary"),
    ("h", "open help"),
    ("Space", "show translation or next text"),
    ("Enter", "save text and translation to dictionary (in add page)"),
    ("esc", "back to main page"),
    ("ctrl-c", "quit the program"),
)

URWID_PALETTE = (
    ("text", "dark blue", ""),
    ("translation", "yellow", ""),
    ("keybinding", "dark cyan", ""),
    ("footer", "light gray", ""),
    ("error", "dark red", ""),
    ("success", "dark green", ""),
)

EMPTY_REQUIRED_FIELDS_ERROR = (
    "To save, you need to fill in both the text and translation fields"
)

SAVING_SUCCESS_MESSAGE = "Saved successfully!"
