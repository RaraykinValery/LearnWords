DB_NAME = "db.sqlite3"

GREEN = "\033[92m"
BLUE = "\033[94m"
RESET_COLOR = "\033[0m"

TEXT_STRING = "{text}" + "\n"
TRANSLATION_STRING = GREEN + "{translation}" + RESET_COLOR + "\n"
HINT_STRING = f"{BLUE}Hit Enter to to continue, Ctrl-c to exit{RESET_COLOR}"

NO_TRANSLATIONS_ERROR = (
    "You have no translations added to your dictionary.\n"
    "Use add parameter to add one."
)
