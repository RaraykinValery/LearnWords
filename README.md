![learn_words2](https://user-images.githubusercontent.com/32908993/223927173-cb9d2d50-ccc8-43bc-8852-19ee51de61c8.gif)

# LearnWords

**LearnWords** is a programm for learning foreign language words and phrases.

# Installation
Clone this git repository:\
```git clone https://github.com/RaraykinValery/LearnWords.git```

Change to the project directory:\
```cd LearnWords```

Install requirements:\
```pip install -r requirements.txt```

# Usage

You can use the program with an absolute path. For example, from the project folder, the command will be: `./LearnWords`

Alternatively, you can add it to PATH and use it everywhere in your system.

The program consists of two functions that can be called from the terminal using the "add" and "learn" parameters.

To add a word "hello" and its translation "привет" to your dictionary, use the following command:\
```LearnWords add hello привет```

Once you have added some words and/or phrases to your dictionary, you can start learning:\
```LearnWords learn```

After running the `LearnWords learn` command, you will see an interface displaying a random word or phrase from your dictionary. Press the "space" key to reveal its translation. If you press the "space" key again, the next random word will appear.

Pressing "a" will allow you to open a form for adding a new word and translation to your dictionary as well.

# Requirements

To use LearnWords, you will need:

- Python 3.10
- Urwid
