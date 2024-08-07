from flask import Flask, render_template, request, redirect, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
from werkzeug.security import generate_password_hash, check_password_hash
import random

from Sistem_Classes_and_Methods.User_Authorization import UserAuthorization
from Sistem_Classes_and_Methods.mail import send_mail
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
    charts = db.Column(db.String())

    def __repr__(self):
        return f"<users {self.id}>"


def allowed_file(filename: str) -> bool:
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
        answer_1 = request.form.get('name')
        answer_2 = request.form.get('nickname')
        answer_3 = request.form.get('password')
        answer_1 = answer_1.title()
        answer_2 = answer_2.title()
        check = UserAuthorization(answer_1, answer_2, answer_3, Users)
        answer = check.user_is_registered()
        if type(answer[0]) == bool:
            session['name'] = answer_1
            session['nickname'] = answer_2
            session['avatar'] = answer[1]
            return redirect('/')
        else:
            return render_template('form_3.html', error=answer[0])


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
        session['user_name'] = answer_1
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
            users = Users(name=session['user_name'], nickname=session['nickname'], password=session['password'],
                          mail=session['mail'], avatar='profil.png')
            db.session.add(users)
            db.session.flush()
            db.session.commit()
            session['avatar'] = 'profil.png'
            session['name'] = session['user_name']
            return redirect("/")
        else:
            return render_template('SMS_form.html', error='Неправильный код', display_none='')


@app.route('/mood/<id>', methods=['GET', 'POST'])
def mood(id):
    nickname = Users.query.filter_by(nickname=session['nickname']).first()
    charts_str = ''
    if nickname.charts != None:
        charts_str = nickname.charts
    charts_str += str(id)
    num_rows_updated = Users.query.filter_by(nickname=session['nickname']).update(
        dict(charts=charts_str))
    db.session.commit()
    return redirect('/')


@app.route('/home', methods=['GET', 'POST'])
def home():
    with open("instance/quotes.txt", "r", encoding="utf-8") as file:
        file_list = file.readlines()
        len_list = len(file_list)
        random_text = file_list[random.randint(0, len_list) - 1]
    if request.method == 'GET':
        return render_template('entrance.html', name=session['name'], profil=session['avatar'], quotes=random_text)
    elif request.method == 'POST':
        if request.form.get('new_name') == None:
            if 'file' not in request.files:
                return redirect(request.url)
            file = request.files['file']
            if file.filename == '':
                return redirect(request.url)
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                session['avatar'] = filename
                num_rows_updated = Users.query.filter_by(nickname=session['nickname']).update(
                    dict(avatar=session['avatar']))
                db.session.commit()
                return render_template('entrance.html', name=session['name'], profil=session['avatar'],
                                       quotes=random_text)
        else:
            new_name = request.form.get('new_name').title()
            num_rows_updated = Users.query.filter_by(nickname=session['nickname']).update(
                dict(name=new_name))
            session['name'] = new_name
            db.session.commit()
            return render_template('entrance.html', name=session['name'], profil=session['avatar'], quotes=random_text)


@app.route('/preloader', methods=['GET', 'POST'])
def preloader():
    return render_template('prelooder.html')


@app.route('/charts', methods=['GET', 'POST'])
def charts():
    nickname = Users.query.filter_by(nickname=session['nickname']).first()
    charts_str = ''
    if nickname.charts != None:
        charts_str = nickname.charts
        level_1 = charts_str.count('1')
        level_2 = charts_str.count('2')
        level_3 = charts_str.count('3')
        level_4 = charts_str.count('4')
        level_5 = charts_str.count('5')
        level_6 = charts_str.count('6')
        level_7 = charts_str.count('7')
        len_str = len(charts_str)
        percentage_ratio_1 = int(level_1 / len_str * 100)
        percentage_ratio_2 = int(level_2 / len_str * 100)
        percentage_ratio_3 = int(level_3 / len_str * 100)
        percentage_ratio_4 = int(level_4 / len_str * 100)
        percentage_ratio_5 = int(level_5 / len_str * 100)
        percentage_ratio_6 = int(level_6 / len_str * 100)
        percentage_ratio_7 = 100 - (
                percentage_ratio_1 + percentage_ratio_2 + percentage_ratio_3 + percentage_ratio_4 + percentage_ratio_5 + percentage_ratio_6)
        return render_template('charts.html', error='', percentage_ratio_1=percentage_ratio_1,
                               percentage_ratio_2=percentage_ratio_2, percentage_ratio_3=percentage_ratio_3,
                               percentage_ratio_4=percentage_ratio_4, percentage_ratio_5=percentage_ratio_5,
                               percentage_ratio_6=percentage_ratio_6, percentage_ratio_7=percentage_ratio_7)
    else:
        return render_template('charts.html', error='Вы не ответили ни на один из вопросов')


if __name__ == "__main__":
    # with app.app_context():
    #     db.create_all()
    app.run()
