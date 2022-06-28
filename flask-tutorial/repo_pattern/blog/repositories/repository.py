from .irepository import IRepository

class Repository(IRepository):
    def __init__(self, db, model=None):
        self.db = db
        self.model = model

    async def get_list_async(self):
        if not self.model is None:
            result = self.model.query.all()
            return result

        return await super().get_list_async()


    async def add_async(self, kwargs):
        
        if not self.model is None:
            result = self.model(**kwargs)
            self.db.session.add(result)
            self.db.session.commit()
            return result

        return await super().add_async(kwargs)

    async def get_async(self, id):
        if not self.model is None:
            result = self.model.query.get(id)
            return result
            
        return await super().get_async(id)


    async def update_async(self, id):
        
        return await super().update_async(id)

    async def delete_async(self, id):
        if not self.model is None:
            result = self.model.query.get(id)
            self.db.session.delete(result)
            self.db.session.commit()
            
            return {"messsage": "Successfully Deleted!"}
    
        return await super().delete_async(id)