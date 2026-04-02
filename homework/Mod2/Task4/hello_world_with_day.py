import argparse

from flask import Flask
from datetime import datetime

weekdays = ('Хорошего понедельника', 'Хорошего вторника', 'Хорошей среды', 'Хорошего четверга',
            'Хорошей пятницы', 'Хорошей субботы', 'Хорошего воскресенья')

app = Flask(__name__)


@app.route('/hello-world/<name>')
def get_correct_username_with_weekdate(name):
    weekday = datetime.today().weekday()
    return f'Hello, {name}. {weekdays[weekday]}!'


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Запуск Flask приложения')
    parser.add_argument('--port', type=int, default=5000, help='Порт для запуска Flask приложения')
    args = parser.parse_args()

    app.run(debug=True, port=args.port)