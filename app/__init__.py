from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config) #reads and applies the Config file
db = SQLAlchemy(app) #db object represents the database
migrate = Migrate(app, db) #represents the migration engine

from app import routes, models #models defines the structure of the database