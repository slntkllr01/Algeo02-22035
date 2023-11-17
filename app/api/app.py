import time
from flask import Flask, jsonify, request, json
from flask_cors import CORS
import traceback
import os
from werkzeug.utils import secure_filename

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

# UPLOAD DATASET
print("Current working directory:", os.getcwd())
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
UPLOAD_FOLDER = os.path.join(BASE_DIR, 'dataset')
# ALLOWED_EXTENSIONS = {'zip', 'tar', 'tar.gz', '.jpeg', '.jpg', '.png'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['CURRENT_IMAGE_FOLDER'] = CURRENT_IMAGE_FOLDER

# def allowed_file(filename):
#     return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload_dataset', methods=['POST'])
def uploadDataset():
    print(request.files)
    if 'file' not in request.files:
        resp = jsonify({
            "message": 'No file part in the request',
            "status": 'success'
        })
        resp.status_code = 400
        return resp   
    
    file = request.files['file']
    if file.filename == '':
        resp = jsonify({
            "message": 'No file selected for uploading',
            "status": 'success'
        })
        resp.status_code = 400
        return resp
    else:
    # if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(BASE_DIR, 'dataset', filename)
        print("Saving file to:", file_path)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        resp = jsonify({
            "message": 'Files successfully uploaded',
            "status": 'success'
        })
        return resp
    return jsonify({'error': 'No selected file'})


@app.route('/process_and_compare', methods=['POST'])
def process_and_compare():
    if 'file' not in request.files:
        resp = jsonify({
            "message": 'No file part in the request',
            "status": 'success'
        })
        resp.status_code = 400
        return resp   
    
    file = request.files['file']
    if file.filename == '':
        resp = jsonify({
            "message": 'No file selected for processing',
            "status": 'success'
        })
        resp.status_code = 400
        return resp
    else:
        # Implement your image processing and comparison logic here
        # Use the uploaded image directly, no need for a separate "current image"
        filename = secure_filename(file.filename)
        current_image_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        
        # Implement your image processing and comparison logic here using current_image_path
        # ...

        resp = jsonify({
            "message": 'Image processed and compared successfully',
            "status": 'success'
        })
        return resp
# @app.route('/post/<int')


    

if __name__ == '__main__':
  app.run(debug=True, port=5000)