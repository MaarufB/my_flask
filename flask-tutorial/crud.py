from datetime import datetime
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///crud.db'

db = SQLAlchemy(app)
ma = Marshmallow(app)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(20), nullable=False, default='N/A')
    date_posted = db.Column(db.DateTime, nullable=True, default=datetime.utcnow)

    def __repr__(self) -> str:
        return self.title

# Post Schema // This is gonna be our serializer
class PostSchema(ma.Schema):
    class Meta:
        fields = ('id', 'title', 'content', 'author')

# Fetching one schema
post_schema = PostSchema()
posts_schema = PostSchema(many=True)

@app.route('/')
# @marshal_with(post_fields)
async def index():
    post = Post.query.all()
    posts_serialized = posts_schema.jsonify(post)
    # we can use jsonify or the Schema
    serialized = posts_schema.dump(post)
    return jsonify(serialized)

@app.route('/add', methods=['POST'])
async def add():
    data = request.json
    post = Post(**data)
    db.session.add(post)
    db.session.commit()
    serialized = post_schema.dump(post)

    return serialized

@app.route('/get/<int:id>')
async def get(id):
    # post = Post.query.filter_by(id=id).first()

    # we can use this approach and also the above approach
    post = Post.query.get(id)
    serialized = post_schema.dump(post)
    return serialized

@app.route('/update/<int:id>', methods=["PUT"])
async def update(id):   
    data = request.json
    post = Post.query.get(id)
    post.title = data['title']
    post.content = data['content']
    post.author = data['author']
    db.session.commit()    
    
    new_post = Post.query.get(id)
    serialized = post_schema.dump(new_post)

    return serialized

@app.route('/delete/<int:id>', methods=["DELETE"])
async def delete(id):
    post = Post.query.get(id)
    db.session.delete(post)
    db.session.commit()

    return {"message": "Successfully deleted!"}

if __name__ == '__main__':
    app.run(debug=True)