from blog import app

@app.route('/another_route')
async def another_route():
    
    return "This is Another Route!"