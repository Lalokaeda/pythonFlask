import subprocess

from flask import Flask
from flask_wtf import FlaskForm
from wtforms.fields.simple import *
from wtforms.fields.numeric import *
from wtforms.validators import InputRequired, NumberRange


app = Flask(__name__)


class CodeForm(FlaskForm):
    code = StringField(validators=[InputRequired()])
    timeout = IntegerField(validators=[InputRequired(), NumberRange(min=1, max=30)])


def code_runer(code: str, timeout: int):
    command = ['prlimit', '--nproc=1:1', 'python', '-c', code]
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    try:
        result, error = process.communicate(timeout=timeout)
        if result:
            return result
        return f'Ошибка при попытке запуска кода:/n{error}', 400
    except subprocess.TimeoutExpired as e:
        process.kill()
        process.communicate()
        return f'Во время выполнения кода был превышен лимит времени: {timeout} секунд ', 500


@app.route('/code_runner', methods=['POST'])
def get_code_and_timeout():
    form = CodeForm()

    if form.validate_on_submit():
        user_code, user_timeout = form.code.data, form.timeout.data
        return code_runer(code=user_code, timeout=user_timeout)

    return f'invalid input{form.errors}', 422


if __name__ == '__main__':
    app.config['WTF_CSRF_ENABLED'] = False
    app.run(debug=True)