from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///blog.db"

# make a db object here to instantiate it
db = SQLAlchemy(app)
ma = Marshmallow(app)
from blog import routes