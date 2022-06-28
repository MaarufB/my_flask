from blog import app, db
from blog.models import Post
from flask import jsonify, request
from blog.schemas import PostSchema

@app.route('/blog/', methods=["GET", "POST"])
async def index():
    schema = PostSchema()
    if request.method == "POST":
        data = request.json
        post = Post(**data)
        res = db.session.add(post)
        commit = db.session.commit() 
        print(f"res {res} commit: {commit}")
        return schema.dump(post) 
    
    blogs = Post.query.all()
    new_blogs = schema.dump(blogs, many=True)
    
    return jsonify(new_blogs)

@app.route('/blog/<int:id>', methods=['GET', 'PUT', 'DELETE'])
async def blog(id):
    schema = PostSchema()
    
    if request.method == "GET":
        post = Post.query.get(id)
        new_post = schema.dump(post)
        return new_post

    elif request.method == "PUT":
        data = request.json
        post = Post.query.get(id)
        post.title = data['title']
        post.content = data['content']
        db.session.commit()
        serialized =schema.dump(post)

        return serialized

    elif request.method == "DELETE":
        post = Post.query.get(id)
        db.session.delete(post)
        db.session.commit()

        return {"message": "Successfully Deleted!!"}

    return {"message": "Bad Request!!"}
