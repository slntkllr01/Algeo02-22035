import time
import sys
from flask import Flask, jsonify, request
from flask_cors import CORS
import traceback
import os
from werkzeug.utils import secure_filename
from lib.CBIR.main import compareImage
# from lib.CBIR.main import compareImage

app = Flask(__name__)
CORS(app)

# print(sys.path)



def format_result(result):
    formatted_result = []
    for item in result:
        # Misalkan tuple berisi (nilai_similarity, file_path)
        similarity, file_path = item
        formatted_item = {
            'similarity': similarity,
            'file_path': file_path,
        }
        formatted_result.append(formatted_item)
    return formatted_result


@app.route('/')
def welcome():
    return 'Welcome to the sangkuLens Tubes!'

@app.route('/time')
def get_current_time():
    return {'time': time.localtime()}

@app.route('/api/hello')
def hello():
    return jsonify({'message': 'Hello, World!'})

file_path = None

# UPLOAD DATASET
print("Current working directory:", os.getcwd())
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
UPLOAD_FOLDER = os.path.join(BASE_DIR, 'dataset')
# ALLOWED_EXTENSIONS = {'zip', 'tar', 'tar.gz', '.jpeg', '.jpg', '.png'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/upload_dataset', methods=['GET','POST'])
def uploadDataset():
    global file_path
    # print(request.files)
    if 'file' not in request.files:
        resp = jsonify({
            "message": 'No file part in the request',
            "status": 'success'
        })
    elif request.files['file'].filename == '':
        resp = jsonify({
            "message": 'No file selected for uploading',
            "status": 'success'
        })
        resp.status_code = 400
    else:
    # if file and allowed_file(file.filename):
        file = request.files['file']
        filename = secure_filename(file.filename)
        file_path = os.path.join(BASE_DIR, 'dataset', filename)
        print("Saving file to:", file_path)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        resp = jsonify({
            "message": 'Files successfully uploaded',
            "status": 'success'
        })
    
    return resp
    # return jsonify({'error': 'No selected file'})


@app.route('/upload_multidata', methods = ['POST'])
def upload_multidata():
    try:
        if "files[]" not in request.files:
            return jsonify({"message": "No files part in the request"}), 400

        files = request.files.getlist("files[]")

        if not files:
            return jsonify({"message": "No files selected for uploading"}), 400

        # Ganti nama folder upload menjadi UPLOAD_DATASET
        folder_path = os.path.join(app.config["UPLOAD_DATASET"], "uploaded_dataset")
        os.makedirs(folder_path, exist_ok=True)

        for file in files:
            filename = secure_filename(file.filename)
            file_path = os.path.join(folder_path, filename)
            file.save(file_path)

        return jsonify({"message": "Files successfully uploaded", "folder_path": folder_path})
    except Exception as error:
        return jsonify({"message": f"Error during upload: {str(error)}"}), 500


@app.route('/process_and_compare', methods=['GET'])
def process_and_compare():
    global file_path
    file_path_temp = request.args.get('file_path', default=None, type=str)
    if file_path_temp is None:
        return jsonify({"error": "Parameter 'file_path' is required"}), 400
    compare_values_to_display = compareImage(file_path_temp, "lib/CBIR/dataset")
    formatted_result = format_result(compare_values_to_display)
    return jsonify(formatted_result)

if __name__ == '__main__':
  app.run(debug=True, port=5000)