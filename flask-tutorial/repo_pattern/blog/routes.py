from flask import request, jsonify
from blog import app
from .mapper import PostSchema
from .repositories import Repository
from .models.blog_model import Post
from blog import db

@app.route('/blogs', methods=["GET", "POST"])
async def blogs():
    post = Repository(db, Post)

    if request.method == "POST":
        data = request.json
        # print(f"DATA: {data}")
        data = await post.add_async(data)
        schema = PostSchema()

        return schema.dump(data)

    elif request.method == "GET":
        result = await post.get_list_async()
        schema = PostSchema()
        serilized = schema.dump(result, many=True) 
        return jsonify(serilized)

    return {
        "message": "Bad Request"
    }

@app.route('/blogs/<int:id>', methods=["GET", "PUT", "DELETE"])
async def blog(id):
    post = Repository(db, Post)

    if request.method == "GET":
        result = await post.get_async(id)
        if result != None:
            schema = PostSchema()
            return schema.dump(result)

        return {"message": "data is no longer exist"}
    
    elif request.method == "PUT":
        result = await post.get_async(id)
        
        if result != None:
            data = request.json
            result.title = data["title"]
            result.body = data["body"]
            db.session.commit()
            schema = PostSchema()

            return schema.dump(result)

        return {"message": "Data is no longer exist!"}

    elif request.method == "DELETE":
        check_if_exist = await post.get_async(id)

        if (check_if_exist != None):
            result = await post.delete_async(id)
            return result

        return {"message": "data is no longer exist!"}

    return {"message": "Bad Request"}