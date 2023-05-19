from config import FULL_URL_DB
from flask import Flask
from flask_migrate import Migrate
from models.user import User
from routes.users import users
from utils.db import db

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = FULL_URL_DB
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

Migrate(app, db)

app.register_blueprint(users)
