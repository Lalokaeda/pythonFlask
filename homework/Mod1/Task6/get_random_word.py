from flask import Flask
from random import choice
import os, re

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BOOK_FILE = os.path.join(BASE_DIR, 'war_and_peace.txt')


def get_all_words(filepath):
    with open(filepath, 'r') as file:
        text = file.read()
        words = re.findall(r'\b\w+\b', text)
        cleaned_words = [word for word in words if re.search(r'[А-Яа-я]', word)]
    return cleaned_words


words_list = get_all_words(BOOK_FILE)


@app.route('/get_random_word')
def get_random_word():
    word = choice(words_list)
    return word


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)