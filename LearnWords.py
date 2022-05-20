import json
import random

class Training_dictionary:
    def __init__(self):
        self.dictionary = self.read_dict()
        self.yes = ["Y", "y", "yes", "YES", "Yes", "YEs", "yeS", "yES", "yEs"]
        self.no = ["N", "n", "not", "NOT", "Not", "NOt", "noT", "nOT", "nOt", "no", "NO"]

    def greetings(self):
        print("WELCOME to LearnWords!")
        print("It's good to see you here!")
        self.menu()

    def menu(self):
        choise = self.ask_answer("Do you want to Learn or Add words? [L/A]")
        if choise in ["L", "l", "learn", "LEARN"]:
            print("Let's learn!")
            self.learn()
        elif choise in ["A", "a", "add", "ADD"]:
            self.add_word()
        else:
            self.ask_answer("Do you want to Learn or Add words? [L/A]")

    def add_word(self):
        word = input("Enter a word: ").strip()
        meaning = input("Enter a meaning: ").strip()
        self.dictionary[word] = meaning
        self.save()
        else_word_answer = self.ask_answer("Your word saved! Another word? [y/n]")
        if else_word_answer in self.yes:
            self.add_word()
        elif else_word_answer in self.no:
            print("Coming back to menu")
            self.menu()

    def learn(self):
        words = list(self.dictionary.keys())
        choice = random.choice(words)
        print(choice)
        input("To show answer press ENTER")
        print(self.dictionary[choice])
        rightness_answer = self.ask_answer("Was your answer right? [y/n]")
        if rightness_answer in self.yes:
            self.learn()
            # right_answers = ("right_answers.txt", "a")
        elif rightness_answer in self.no:
            self.learn()

    def ask_answer(self, question):
        answer = input(question + " ").strip()
        return answer

    def read_dict(self):
        train_dictionary_r = open("train_dictionary.txt", "r") #нужен относительный расположению скрипта путь
        train_dictionary_json = train_dictionary_r.readline()
        train_dictionary = json.loads(train_dictionary_json)
        train_dictionary_r.close()
        return train_dictionary

    def save(self):
        current_dictionary = json.dumps(self.dictionary, ensure_ascii=False)
        train_dictionary_a = open("train_dictionary.txt", "w")
        train_dictionary_a.write(current_dictionary)
        train_dictionary_a.close()


if __name__ == "__main__":
    your_dictionary = Training_dictionary()
    your_dictionary.greetings()
