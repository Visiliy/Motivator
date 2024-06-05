from flask import Flask, render_template, request, redirect, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SECRET_KEY'] = '5457fae2a71f9331bf4bf3dd6813f90abeb33839f4608755ce301b9321c671791673817685w47uer6uuu'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(app)


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(30))
    nickname = db.Column(db.String(30))
    password = db.Column(db.String(30))
    mail = db.Column(db.String(100))

    def __repr__(self):
        return f"<users {self.id}>"


@app.route('/')
def index():
    name = ''
    if 'name' in session:
        name = session['name']
    return render_template('main.html', name=name)


@app.route('/entrance', methods=['GET', 'POST'])
def entrance():
    if request.method == 'GET':
        return render_template('form_3.html')

    elif request.method == 'POST':
        answer_1 = request.form.get('name')
        answer_2 = request.form.get('nickname')
        answer_3 = request.form.get('password')
        answer_4 = request.form.get('mail')
        answer_1 = answer_1.title()
        answer_2 = answer_2.title()
        return redirect('/sms_code')


@app.route('/registrations', methods=['GET', 'POST'])
def registrations():
    if request.method == 'GET':
        return render_template('form_2.html')
    elif request.method == 'POST':
        answer_1 = request.form.get('name')
        answer_2 = request.form.get('nickname')
        answer_3 = request.form.get('password')
        answer_4 = request.form.get('repeat_the_password')
        answer_5 = request.form.get('mail')
        answer_1 = answer_1.title()
        answer_2 = answer_2.title()
        pass_1 = generate_password_hash(answer_3)
        users = Users(name=answer_1, nickname=answer_2, password=pass_1, mail=answer_5)
        db.session.add(users)
        db.session.flush()
        db.session.commit()
        session['name'] = answer_1
        session['nickname'] = answer_2
        session['password'] = answer_3
        session['mail'] = answer_5
        return redirect('/sms_code')


@app.route('/sms_code', methods=['GET', 'POST'])
def sms_code():
    if request.method == 'GET':
        return render_template('SMS_form.html')
    elif request.method == 'POST':
        return redirect('/')


if __name__ == "__main__":
    app.run()
