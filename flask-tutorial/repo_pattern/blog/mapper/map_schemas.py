from blog import ma

class PostSchema(ma.Schema):
    class Meta:
        fields = ["id", "title", "body"]