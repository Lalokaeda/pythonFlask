import shlex

from flask import Flask, request
import subprocess

app = Flask(__name__)


@app.route('/ps', methods=['GET'])
def ps():
    args: list[str] = request.args.getlist('arg')
    clean_args = [shlex.quote(arg) for arg in args]
    command = ["ps"] + clean_args
    try:
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=False)
        if result.returncode == 0:
            return f'<pre>{result.stdout}</pre>'
        else:
            return f'Команда завершена с ошибкой: {result.stderr}', 400
    except Exception as e:
        return f'Произошла ошибка при выполнении команды: {e}', 500


if __name__ == '__main__':
    app.config['WTF_CSRF_ENABLED'] = False
    app.run(debug=True)