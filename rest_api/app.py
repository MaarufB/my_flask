from flask import Flask, request
from flask_restful import Resource, Api, marshal_with, fields
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
api = Api(app)

app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///todo.db'
db = SQLAlchemy(app)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)

    def __repr__(self) -> str:
        return self.name

fake_database = {
    1:{'name':'Clean Car'},
    2:{'name': 'Write blog'},
    3:{'name': 'Start stream'}
}

task_fields = {
    "id": fields.Integer,
    "name":fields.String, 
}

class Items(Resource):
    @marshal_with(task_fields)
    def get(self):
        tasks = Task.query.all()
        return tasks

    @marshal_with(task_fields)
    def post(self):
        data = request.json
        print(f"DATA: {data}")
        task = Task(name=data['name'])
        db.session.add(task)
        db.session.commit()
        return task

class Item(Resource):
    @marshal_with(task_fields)
    def get(self, pk):
        task = Task.query.filter_by(id=pk).first()
        return task

    @marshal_with(task_fields)
    def put(self, pk):
        data = request.json 
        task = Task.query.filter_by(id=pk).first()
        task.name = data['name']
        db.session.commit()
        
        return task

    @marshal_with(task_fields)
    def delete(self, pk):
        task = Task.query.filter_by(id=pk).first()
        db.session.delete(task)
        db.session.commit()
        tasks = Task.query.all()
        
        return  tasks

api.add_resource(Items, '/')
api.add_resource(Item, '/<int:pk>/')


if __name__ == '__main__':
    app.run(debug=True)