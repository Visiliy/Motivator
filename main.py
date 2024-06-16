from flask import Flask, render_template, request, redirect, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
from werkzeug.security import generate_password_hash, check_password_hash
import random
from mail import send_mail
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = '5457fae2a71f9331bf4bf3dd6813f90abeb33839f4608755ce301b9321c671791673817685w47uer6uuu'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(app)
UPLOAD_FOLDER = 'static/img/'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(30))
    nickname = db.Column(db.String(30))
    password = db.Column(db.String(30))
    mail = db.Column(db.String(100))
    avatar = db.Column(db.String(200))

    def __repr__(self):
        return f"<users {self.id}>"


def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/exit')
def exit():
    session.clear()
    return redirect("/")


@app.route('/')
def index():
    name = ''
    sicret_cod = 'no'
    profile = 'profil.png'
    if 'name' in session:
        name = session['name']
        sicret_cod = 'yes'
    if 'avatar' in session:
        profile = session['avatar']
    return render_template('main.html', name=name, profile=profile, sicret_cod=sicret_cod)


@app.route('/entrance', methods=['GET', 'POST'])
def entrance():
    if request.method == 'GET':
        return render_template('form_3.html', display_none='display: none;')

    elif request.method == 'POST':
        error = ''
        answer_1 = request.form.get('name')
        answer_2 = request.form.get('nickname')
        answer_3 = request.form.get('password')
        answer_1 = answer_1.title()
        answer_2 = answer_2.title()
        nickname = Users.query.filter_by(nickname=answer_2).first()
        if nickname:
            if nickname.name == answer_1 and check_password_hash(nickname.password, answer_3):
                session['name'] = answer_1
                session['nickname'] = answer_2
                session['avatar'] = nickname.avatar
                return redirect('/')
            else:
                error = 'Неправльно введены имя и/или пароль'
                return render_template('form_3.html', error=error)
        else:
            error = 'Вас нет в системе, зарегистрируйтесь'
            return render_template('form_3.html', error=error)


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
        cod = random.randint(10000, 99999)
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
                          mail=session['mail'], avatar='profil.png')
            db.session.add(users)
            db.session.flush()
            db.session.commit()
            session['avatar'] = 'profil.png'
            return redirect("/")
        else:
            return render_template('SMS_form.html', error='Неправильный код', display_none='')


@app.route('/mood/<id>', methods=['GET', 'POST'])
def mood(id):
    print(id)
    return redirect('/')


@app.route('/home', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        return render_template('entrance.html', name=session['name'], profil=session['avatar'])
    elif request.method == 'POST':
        if request.form.get('new_name') is None:
            if 'file' not in request.files:
                print('ok_1')
                return redirect(request.url)
            file = request.files['file']
            if file.filename == '':
                print('ok_2')
                return redirect(request.url)
            if file and allowed_file(file.filename):
                print('ok_3')
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                session['avatar'] = filename
                num_rows_updated = Users.query.filter_by(nickname=session['nickname']).update(
                    dict(avatar=session['avatar']))
                db.session.commit()
                return render_template('entrance.html', name=session['name'], profil=session['avatar'])
        else:
            new_name = request.form.get('new_name')
            num_rows_updated = Users.query.filter_by(nickname=session['nickname']).update(
                dict(name=new_name))
            session['name'] = new_name
            db.session.commit()


if __name__ == "__main__":
    app.run()
