class CanNotCreateDatabase(Exception):
    """Program can't create database"""


class CanNotAddTextAndTranslation(Exception):
    """Programm can't add a text and it's translation to database"""


class CanNotDeleteTextAndTranslation(Exception):
    """Programm can't delete a text and it's translation from database"""


class CanNotGetTextAndTranslation(Exception):
    """Programm can't get a text and it's translation from database"""
