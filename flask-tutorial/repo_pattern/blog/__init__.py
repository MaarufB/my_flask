from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from asgiref.wsgi import WsgiToAsgi

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///blog.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# make a db object here to instantiate it
db = SQLAlchemy(app)
ma = Marshmallow(app)

from blog import routes
# from blog import routes_2

# The code below have problems need to fix soon
# app.add_url_rule('/blogs', view_func=routes.blogs)
# app.add_url_rule('/blog', view_func=routes.blog)

asgi_app = WsgiToAsgi(app)