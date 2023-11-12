import time
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def welcome():
    return 'Welcome to the sangkuLens Tubes!'

@app.route('/time')
def get_current_time():
    return {'time': time.localtime()}

@app.route('/api/hello')
def hello():
    return jsonify({'message': 'Hello, World!'})

if __name__ == '__main__':
  app.run(debug=True, port=5000)