from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# import __main__

app = Flask(__name__)

# This should be imported below the app object
from myproject import routes