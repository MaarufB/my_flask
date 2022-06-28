from flask import Flask, request, jsonify


# if you want to use flask as backend for SPA
# it would be good if jsonify the return object

app = Flask(__name__)

@app.route('/')
async def index():
    context = {
        'status': 'Healthy'
    }
    return jsonify(context)


if __name__ == '__main__':
    app.run(debug=True)