# FILE NO # 6
# this code is incase we wanted to predect the label of one image

from PIL import Image
from matplotlib.image import imread
from KNN import *
import glob
import os

# img = Image.open("javed.png")                 # we load the image here
# img = img.resize((64, 64), Image.ANTIALIAS)   # we resize the image here
# img = img.convert('L')                        # we convert to gray scale
# img.save("jojo.png")                          # we save the processed image

jojo = imread('jojo.png')                       # we read the processed image

# print(jojo.size,jojo.shape,jojo.ndim)

X = np.load("data_set.npy")   # we load the original data set
Y = np.load("labels.npy")      # we load the labels of the original data set

k =1    # number of clusters
clus = K_Nearest_Nighbor(k=k)     # call the class from KNN
clus.cluster(X, Y)                # call the clustering functon
predictions = clus.prediction(jojo) # call the predection function

# if else , to predict if it is a cat of a dog
if predictions == 1:
    print("it is KUTTA ")
else:
    print("it is BELLI ")