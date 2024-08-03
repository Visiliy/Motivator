from werkzeug.security import check_password_hash


class UserAuthorization:
    def __init__(self, name: str, nickname: str, password: str, db_name) -> None:
        self.name = name
        self.nickname = nickname
        self.password = password
        self.db_name = db_name

    def user_is_registered(self) -> tuple:
        nickname_in_db = self.db_name.query.filter_by(nickname=self.nickname).first()
        if nickname_in_db:
            if nickname_in_db.name == self.name and check_password_hash(nickname_in_db.password, self.password):
                return True, nickname_in_db.avatar
            else:
                return 'Неправльно введены имя и/или пароль',
        else:
            return 'Вас нет в системе, зарегистрируйтесь',
