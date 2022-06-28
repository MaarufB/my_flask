from flask import Flask
from Models import db, EmployeeModel

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'employee.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app) 

@app.before_first_request
def create_table():
    db.create_all()

app.run(host='localhost', port=5000)