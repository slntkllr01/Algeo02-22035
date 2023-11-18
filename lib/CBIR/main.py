import numpy as np  
import cv2
import os 
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
# from PIL import Image

from byTexture import *
from byColor import*


reference_image_path = "lib/CBIR/0.jpg" 
folder_path = "lib/CBIR/datasetByTexture" 


def compareImage(reference_image_path,folder_path):
    reference_image = cv2.imread(reference_image_path)
    reference_image = cv2.resize(reference_image, (256, 256))
    reference_features = getTextureFeatures(reference_image)

    # Get the list of files in the folder
    image_files = [f for f in os.listdir(folder_path)]

    # Initialize an array to store compareByTexture values
    compare_value = 0
    compare_values_to_display = []
    sorted_compare_value_to_display = []
    start = time.time()
    for image_file in image_files:
        # Construct the full path to the image file
        image_path = os.path.join(folder_path, image_file)
        print(image_path)

        # Read the current image
        current_image = cv2.imread(image_path)
        current_image = cv2.resize(current_image, (256, 256))

        # Get texture features for the current image
        current_features = getTextureFeatures(current_image)

        # Compare texture features and store the result in the array
        compare_value = compareByTexture(reference_features, current_features)
        if(compare_value>0.6):
            compare_value*=100
            compare_values_to_display.append((compare_value,image_path))

        # Urutkan compare_values_to_display berdasarkan nilai similarity (descending)
        sorted_compare_value_to_display = sorted(compare_values_to_display, key=lambda x: x[0], reverse=True)

    # end = time.time()
    # print("Time taken to compare", len(image_files), "images:", end - start, "seconds")
    return  (sorted_compare_value_to_display)

# print(compareImage( "lib/CBIR/0.jpg","lib/CBIR/datasetByTexture"))








"""
misal texture
feature query = get texture feature si img query
bikin array similarity[]
loop through dataset
    arraysimilarity [i]= compare similarity (get texture feature (img i), feature query)

display yang similarity >60% from arraysimilarity

[[simil,path]]


"""