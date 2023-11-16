import numpy as np  
import cv2
import os 
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
# from PIL import Image

from byTexture import *
from byColor import*

# source = "lib/CBIR/0.jpg" 
# dataset2 = "lib/CBIR/dataset/4.jpg" 

# dataset_dir = "lib/CBIR/dataset"
# image_list= []

# upload image


# for filename in os.listdir(dataset_dir):
#     if filename.endswith(".jpg"):
#         image_path = os.path.join(dataset_dir, filename)
#         image = cv2.imread(image_path)  # atau PIL.Image.open(image_path) untuk Pillow
#         image = cv2.resize(image,(64,64))
#         image_list.append(image)
# print(image_list)
 


# source = "lib/CBIR/0.jpg" 
# dataset2 = "lib/CBIR/dataset/4.jpg" 
# image= cv2.imread(source)
# image = cv2.resize(image,(256,256))
# feature = getTextureFeatures(image)
# print(feature)


# image2= cv2.imread(dataset2)
# image2 = cv2.resize(image2,(256,256))
# feature2 = getTextureFeatures(image2)
# print(feature2)

# nilai = compareByTexture(feature, feature2)
# print(nilai)

reference_image_path = "lib/CBIR/0.jpg" 
folder_path = "lib/CBIR/dataset" 

reference_image = cv2.imread(reference_image_path)
reference_image = cv2.resize(reference_image, (256, 256))
reference_features = getTextureFeatures(reference_image)

# Get the list of files in the folder
image_files = [f for f in os.listdir(folder_path)]

# Initialize an array to store compareByTexture values
compare_values = []
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
    compare_values.append(compare_value)
end = time.time()
print(compare_values[:10])
print("Time taken to compare", len(image_files), "images:", end - start, "seconds")








"""
misal texture
feature query = get texture feature si img query
bikin array similarity[]
loop through dataset
    arraysimilarity [i]= compare similarity (get texture feature (img i), feature query)

display yang similarity >60% from arraysimilarity

[[simil,path]]


"""