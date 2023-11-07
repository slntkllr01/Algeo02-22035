import numpy as np  
import cv2
import os 

from byTexture import *

# dataset = "lib/CBIR/dataset/0.jpg" 
# dataset2 = "lib/CBIR/dataset/4734.jpg" 

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



# image= cv2.imread(dataset)
# image = cv2.resize(image,(64,64))
# # print(image)
# feature = getTextureFeatures(image)
# print(feature)


# image2= cv2.imread(dataset2)
# image2 = cv2.resize(image2,(64,64))
# # print(image)
# feature2 = getTextureFeatures(image2)
# print(feature2)

# nilai = compareByTexture(feature, feature2)
# print(nilai)








"""
misal texture
feature query = get texture feature si img query
bikin array similarity[]
loop through dataset
    arraysimilarity [i]= compare similarity (get texture feature (img i), feature query)

display yang similarity >60% from arraysimilarity

[[simil,path]]


"""