import time
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/time')
def get_current_time():
    return {'time': time.localtime()}

@app.route('api/hello')
def hello():
    return jsonify({'message': 'Hello, World!'})

if __name__ == '__main__':
    app.run(debug=True)