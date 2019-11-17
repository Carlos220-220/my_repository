from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from flask_restful import Api

app = Flask(__name__)
api = Api(app)

base_path = os.path.abspath(os.path.dirname(__file__))

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///"+os.path.join(base_path,"orm.sqlite3")
app.config["SQLALCHEMY_COMMIT_ON_TEARDOWN"] = True
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

db = SQLAlchemy(app)
