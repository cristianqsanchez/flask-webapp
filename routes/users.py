from flask import Blueprint, render_template, request, redirect, url_for
from models.user import User
from utils.db import db
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import update

users = Blueprint('users', __name__)


@users.route('/')
def index():
    return render_template('index.html')


@users.route('/new', methods=['POST'])
def sing_in():
    username = request.form['username']
    password = request.form['password']

    hashed_password = generate_password_hash(password, )
    new_user = User(username, hashed_password)

    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for('users.login'))


@users.route('/login')
def login():
    return render_template('login.html')


@users.route('/newlogin', methods=['POST'])
def acces():
    username = request.form['username']
    password = request.form['password']

    db_user = User.query.filter_by(username=username).first()
    db_password = db_user.password

    is_correct_password = check_password_hash(db_password, password)

    if db_user and is_correct_password:
        return redirect(url_for('users.home'))

    return render_template('login.html', msg='wrong username or password')


@users.route('/users')
def home():
    users = User.query.all()
    return render_template('users.html', users=users)


@users.route('/user/<string:id>/')
def user(id):
    user = User.query.filter_by(id=id).first()
    return render_template('[userId].html', user=user)

@users.route('/edit/<string:id>/', methods=['POST'])
def edit(id):

    username = request.form['username']
    password = request.form['password']

    
    hashed_password = generate_password_hash(password, )

    user = User.query.filter_by(id=id).first()
    user.username = username
    user.password = hashed_password

    
    db.session.add(user)
    db.session.commit()


    return redirect(url_for('users.home'))

