import argparse

from flask import Flask

app = Flask(__name__)


@app.route('/max_number/<path:subpath>')
def get_max(subpath:str):
    numbers = subpath.split('/')
    try:
        max_number = max(int(number) for number in numbers)
    except ValueError:
        return 'Получен неверный URL, укажите URL в виде \'/max_number/[0-9.*]/[0-9.*]...\''
    return f'Максимальное число: {max_number}'


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Запуск Flask приложения')
    parser.add_argument('--port', type=int, default=5000, help='Порт для запуска Flask приложения')
    args = parser.parse_args()

    app.run(debug=True, port=args.port)