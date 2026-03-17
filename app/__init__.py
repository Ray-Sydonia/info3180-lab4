from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from .config import Config
# import flask migrate here

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
from flask_migrate import Migrate 
# Instantiate Flask-Migrate library here

# Flask-Login login manager
migrate = Migrate(app, db)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

from app import views
