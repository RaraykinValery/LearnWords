import json
import random
import os

class Training_dictionary:
    def __init__(self):
        self.dictionary = self.read_dict()
        self.right_answers = self.read_right_answers()
        self.yes = ["Y", "y", "yes", "YES", "Yes", "YEs", "yeS", "yES", "yEs"]
        self.no = ["N", "n", "not", "NOT", "Not", "NOt", "noT", "nOT", "nOt", "no", "NO"]

    def read_right_answers(self):
        file = open('right_answers.txt', 'r')
        right_answers = []
        for word in file:
            right_answers.append(word.strip())
        return right_answers

    def greetings(self):
        print("WELCOME to LearnWords!")
        print("It's good to see you here!\n")
        self.menu()

    def menu(self):
        print("What do you want to do?")
        print("  l - learn words")
        print("  a - add words")
        print("  r - reset your right answers")
        print("  q - exit")
        choice = self.ask_answer("Enter your answer:")
        if choice in ["L", "l", "learn", "LEARN"]:
            print("Let's learn!")
            self.learn()
        elif choice in ["A", "a", "add", "ADD"]:
            self.add_word()
        elif choice in ["q", "quite"]:
            byes = ["Buy!", "See you!", "See you later!", "Later!",
                    "See you later, aligator!", "Don't forget! With greate power comes great responsibility."]
            print(random.choice(byes))
        elif choice in ["r", "reset"]:
            self.reset()
            print("Your dictionary is successfully reseted!")
            self.menu()
        else:
            self.menu()

    def reset(self):
        with open("right_answers.txt", "w") as ra:
            ra.write("")

    def add_word(self):
        '''Check if the entered word is in the dictionary already'''
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
        while choice in self.right_answers:
            choice = random.choice(words)
        print(choice)
        input("To show answer press ENTER")
        print(self.dictionary[choice])
        rightness_answer = self.ask_answer("Was your answer right? [y/n]")
        if rightness_answer in self.yes:
            self.right_answers.append(choice)
            with open('right_answers.txt', 'a') as ra:
                ra.write(choice + '\n')
            self.learn()
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
    if not os.path.exists("train_dictionary.txt"):
        with open("train_dictionary.txt", "w") as td:
            td.write("{}")
    your_dictionary = Training_dictionary()
    your_dictionary.greetings()
