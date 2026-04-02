from flask import Flask
import argparse

app = Flask(__name__)

visit_counter = 0


@app.route('/counter')
def counter():
    global visit_counter
    visit_counter += 1
    return f'<h1>{visit_counter}<h1>'


# Run this script as: `python .\get_mean_size.py --port=5555` by using argparse
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Запуск Flask приложения')
    parser.add_argument('--port', type=int, default=5000, help='Порт для запуска Flask приложения')
    args = parser.parse_args()

    app.run(debug=True, port=args.port)