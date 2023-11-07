import numpy as np  
import cv2
import os 




dataset = "lib/CBIR/dataset/0.jpg"
# image_list = []
# for filename in os.listdir(dataset):
#     if(filename)
image= cv2.imread(dataset)
image = cv2.resize(image,(50,50))
print(image)



"""
misal texture
feature query = get texture feature si img query
bikin array similarity[]
loop through dataset
    arraysimilarity [i]= compare similarity (get texture feature (img i), feature query)

display yang similarity >60% from arraysimilarity

[[simil,path]]


"""