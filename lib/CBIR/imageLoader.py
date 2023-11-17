import numpy as np  
import cv2
import os 
import time
import concurrent.futures
from byTexture import *
from byColor import*

reference_image_path = "lib/CBIR/0.jpg" 

folder_path = "lib/CBIR/datasetByTexture" 

reference_image = cv2.imread(reference_image_path)
reference_image = cv2.resize(reference_image, (256, 256))
reference_features = getTextureFeatures(reference_image)

# Get the list of files in the folder
image_files = [f for f in os.listdir(folder_path)]

# Initialize an array to store compareByTexture values
compare_values = []

def process_image(image_file):
    image_path = os.path.join(folder_path, image_file)
    print(image_path)
    current_image = cv2.imread(image_path)
    if current_image is not None:
        current_image = cv2.resize(current_image, (256, 256))
        current_features = getTextureFeatures(current_image)
        compare_value = compareByTexture(reference_features, current_features)
        return compare_value

start = time.time()
with concurrent.futures.ThreadPoolExecutor(max_workers=8) as executor:
    futures = {executor.submit(process_image, image_file): image_file for image_file in image_files}
    for future in concurrent.futures.as_completed(futures):
        image_file = futures[future]
        try:
            compare_value = future.result()
            compare_values.append(compare_value)
        except Exception as exc:
            print(f"Error processing {image_file}: {exc}")
        
end = time.time()
print(compare_values[:10])
print("Time taken to compare", len(image_files), "images:", end - start, "seconds")