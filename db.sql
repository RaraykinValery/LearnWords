CREATE TABLE dictionary (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    primary_text varchar(255) NOT NULL,
    translation varchar(255) NOT NULL
);

INSERT INTO dictionary (primary_text, translation) values("hello", "привет");
INSERT INTO dictionary (primary_text, translation) values("How are you?", "Как ты?");
INSERT INTO dictionary (primary_text, translation) values("word", "слово");
INSERT INTO dictionary (primary_text, translation) values("supersititous", "суеверный");