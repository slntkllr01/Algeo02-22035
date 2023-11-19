import time
import sys
from flask import Flask, jsonify, request
from flask_cors import CORS
import traceback
import os
from werkzeug.utils import secure_filename
from algeo.CBIR.compare import *

app = Flask(__name__, static_folder='static',static_url_path='/static')
CORS(app)

# print(sys.path)

# app = Flask(__name__)
# CORS(app)

def format_result(result):
    if result is None:
        return jsonify({'error': 'Comparison result is None'})
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

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

file_path = os.path.join(BASE_DIR,'dataset')
#image
folder_path = os.path.join(BASE_DIR, 'uploaded_dataset')
#dataset


# UPLOAD DATASET
print("Current working directory:", os.getcwd())
UPLOAD_FOLDER = os.path.join(BASE_DIR, 'dataset')
UPLOAD_DATASET = os.path.join(BASE_DIR,'uploaded_dataset')
# ALLOWED_EXTENSIONS = {'zip', 'tar', 'tar.gz', '.jpeg', '.jpg', '.png'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['UPLOAD_DATASET'] = UPLOAD_DATASET



@app.route('/upload_dataset', methods=['POST'])
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

        file_path = os.path.join(BASE_DIR, 'static/dataset', filename)
        print("Saving file to:", file_path)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], file_path))
        resp = jsonify({
            "message": 'Files successfully uploaded',
            "status": 'success'
        })
    
    return resp


@app.route('/upload_multidata', methods = ['POST'])
def upload_multidata():
    global folder_path
    try:
        if "files[]" not in request.files:
            return jsonify({"message": "No files part in the request"}), 400

        files = request.files.getlist("files[]")
        if not files:
            return jsonify({"message": "No files selected for uploading"}), 400

        # Ganti nama folder upload menjadi UPLOAD_DATASET
        folder_path = os.path.join(BASE_DIR, "static/uploaded_dataset")
        os.makedirs(folder_path, exist_ok=True)

        for file in files:
            # file = request.files['file']
            filename = file.filename
            # folder_path = os.path.join(BASE_DIR,'multidataset', filename)
            file.save(os.path.join(folder_path, filename))
            # print(file)

        return jsonify({"message": "Files successfully uploaded", "folder_path": folder_path})
    except Exception as error:
        return jsonify({"message": f"Error during upload: {str(error)}"}), 500


@app.route('/process_and_compare', methods=['GET'])
def process_and_compare():
    global folder_path
    global file_path
    compareType = request.args.get('compareType') 
    compare_values_to_display = None 
    results = []
    file_path_temp = os.path.abspath('.')
    file_path_temp = os.path.join(file_path_temp, 'static/dataset')
    folder_path_temp = os.listdir(file_path_temp)
    # folder_path_temp = request.args.get(folder_path, default=None)

    if file_path_temp is None or folder_path_temp is None:
        return jsonify({"error": f"Parameter {folder_path} is required"}), 400

    # buat pengkondisian jika button yang dipencet 'Color' nanti masuk ke fungsi compareByColor dan sebaliknya, lakukan, lakukan pengkondisian baru looping buat compare 
    for filename in folder_path_temp :
        if compareType == 'Texture':
            compare_values_to_display = compareImageByTexture('static/dataset/'+filename, 'static/uploaded_dataset')
        elif compareType == 'Color':
            compare_values_to_display = compareImageByColor('static/dataset/'+filename, 'static/uploaded_dataset')
        else :
            print(compareType)
        # print(filename)
        # compare_values_to_display = compareImage("dataset/download_image_1698886305127.png", 'uploaded_dataset')
        if compare_values_to_display is not None:
            formatted_result = format_result(compare_values_to_display)
            results.append(formatted_result)
    
    if not results:
        return jsonify({'error': 'No valid results to display'})
    else:
        return jsonify(results[0])

if __name__ == '__main__':
  app.run(debug=True, port=5000)
