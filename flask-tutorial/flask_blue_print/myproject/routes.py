from myproject import app


"""
    this module must be imported by __init__.py
"""


@app.route("/")
async def index():
    return "Flask Blue Prints"