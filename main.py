from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('main.html')


@app.route('/entrance', methods=['GET', 'POST'])
def entrance():
    if request.method == 'GET':
        return render_template('entrance.html')


@app.route('/registrations', methods=['GET', 'POST'])
def registrations():
    if request.method == 'GET':
        return render_template('registrations.html')


if __name__ == "__main__":
    app.run()
