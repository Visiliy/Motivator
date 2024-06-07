from flask import Flask, render_template, request, redirect, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import random
from mail import send_mail

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
    profile = 'profil.png'
    if 'name' in session:
        name = session['name']
    return render_template('main.html', name=name, profile=profile)


@app.route('/entrance', methods=['GET', 'POST'])
def entrance():
    if request.method == 'GET':
        return render_template('form_3.html', display_none='display: none;')

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
        return render_template('form_2.html', display_none='display: none;')
    elif request.method == 'POST':
        error = ''
        answer_1 = request.form.get('name')
        answer_2 = request.form.get('nickname')
        answer_3 = request.form.get('password')
        answer_4 = request.form.get('repeat_the_password')
        answer_5 = request.form.get('mail')
        answer_1 = answer_1.title()
        answer_2 = answer_2.title()
        if Users.query.filter_by(nickname=answer_2).first():
            error += 'Такой никнейм есть, придумайте другой'
        if answer_3 != answer_4:
            if error != '':
                error += '.  '
            error += 'Пароли не совпадают'
        if error != '':
            return render_template('form_2.html', display_none='', error=error)
        pass_1 = generate_password_hash(answer_3)
        session['name'] = answer_1
        session['nickname'] = answer_2
        session['password'] = pass_1
        session['mail'] = answer_5
        return redirect('/sms_code')


@app.route('/sms_code', methods=['GET', 'POST'])
def sms_code():
    if request.method == 'GET':
        cod = random.randint(10000, 100000)
        session['cod'] = str(cod)
        email = session['mail']
        if send_mail(email, 'Код подтверждения', f'Ваш код: {cod}'):
            return render_template('SMS_form.html', error='', display_none='display: none;')
        else:
            return render_template('SMS_form.html', error='Проблема при отправки sms', display_none='')
    elif request.method == 'POST':
        cod_1 = request.form.get('cod_1')
        cod_2 = request.form.get('cod_2')
        cod_3 = request.form.get('cod_3')
        cod_4 = request.form.get('cod_4')
        cod_5 = request.form.get('cod_5')
        cod = f'{cod_1}{cod_2}{cod_3}{cod_4}{cod_5}'
        if cod == session['cod']:
            session.pop('cod')
            users = Users(name=session['name'], nickname=session['nickname'], password=session['password'],
                          mail=session['mail'])
            db.session.add(users)
            db.session.flush()
            db.session.commit()
            return redirect("/")
        else:
            return render_template('SMS_form.html', error='Неправильный код', display_none='')


if __name__ == "__main__":
    app.run()
