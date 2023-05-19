from utils.db import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(250))
    password = db.Column(db.String(250))

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __str__(self):
        return (
            f'id:{self.id},'
            f'username:{self.username},'
            f'password:{self.password}'
        )
