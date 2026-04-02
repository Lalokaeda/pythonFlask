import argparse

from flask import Flask
from datetime import datetime

app = Flask(__name__)
storage = {}


@app.route('/add/<date>/<int:number>')
def add_transaction(date, number):
    date = datetime.strptime(date, '%Y%m%d')
    storage.setdefault(date.year, {}).setdefault(date.month, 0)
    storage[date.year][date.month] += abs(number)
    return f'За период {date.month}/{date.year} добавлена транзакция на сумму {number}'


@app.route('/calculate/<int:year>', defaults={'month': None})
@app.route('/calculate/<int:year>/<int:month>')
def calculate(year, month):
    period = f'{month}/{year}' if month else year
    try:
        if not month:
            expenses = sum(storage[year][m] for m in storage[year])
        else:
            expenses = storage[year][month]
    except KeyError:
        return f'За период {period} не было совершено трат'

    return f'За период {period} траты составили {expenses}'


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Запуск Flask приложения')
    parser.add_argument('--port', type=int, default=5000, help='Порт для запуска Flask приложения')
    args = parser.parse_args()

    app.run(debug=True, port=args.port)