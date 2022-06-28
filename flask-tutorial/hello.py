from flask import Flask
from math_class import Math
from asgiref.wsgi import WsgiToAsgi
from flask import request

app = Flask(__name__)


@app.route('/', methods=('GET', 'POST'))
async def hello():
    # print(app.name) # this will print hello because our file is hello.py
    print(f"{request.method}")
    
    file = None
    return "Hello World!"

@app.route('/get_sum')
async def get_sum(request):
    count_req = 0
    calc = Math()
    loop_response = await calc.loop(100)
    sum = await calc.sum(1,2)
    context = {
        'sum': loop_response
    }
    count_req += 1
    print(count_req)

    return context
@app.route('/upload', methods=('POST',))
async def upload():
    if 'file' not in request.files:
        return {'message': 'There is no file'}
    # else:

    file = request.files['file']
    file.save(f'{file.filename}')
    print(f"file filename: {file.filename}")        
    return str(file.filename)
# asgi_app = WsgiToAsgi(app)

if __name__ == "__main__":
    app.run(debug=True)