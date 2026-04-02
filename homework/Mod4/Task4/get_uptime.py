import subprocess
from flask import Flask


app = Flask('__name__')


@app.route('/uptime')
def get_uptime():
    command = ['uptime', '-p']
    result = subprocess.run(command, stdout=subprocess.PIPE, text=True)
    uptime = result.stdout.strip().replace('up ', '')
    return f'Current uptime is {uptime}'


if __name__ == '__main__':
    app.run(debug=True)