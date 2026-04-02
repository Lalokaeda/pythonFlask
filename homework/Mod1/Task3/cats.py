from flask import Flask
from random import choice

app = Flask(__name__)
cat_list = ['корниш-рекс', 'русская голубая', 'шотландская вислоухая', 'мейн-кун', 'манчкин']


@app.route('/cats')
def cats():
    return choice(cat_list)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
    