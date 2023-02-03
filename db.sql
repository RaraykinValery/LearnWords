CREATE TABLE dictionary (
    id integer PRIMARY KEY,
    primary_text varchar(255) NOT NULL UNIQUE,
    translation varchar(255) NOT NULL
);

INSERT INTO dictionary (primary_text, translation) values("hello", "привет");
INSERT INTO dictionary (primary_text, translation) values("How are you?", "Как ты?");
INSERT INTO dictionary (primary_text, translation) values("word", "слово");
INSERT INTO dictionary (primary_text, translation) values("supersititous", "суеверный");
INSERT INTO dictionary (primary_text, translation)
    values("Derek watched haughtily as Dwight struggled to get out of the box", "Дерек с надменным видом с наблюдал, как Дуайт пытается выбраться из коробки");
