# FILE NO # 4

# this file contains the main algorithem of K nearest nighbor
# from this file I'll import the class to cluster the data and test the accuracy with a some test data

from collections import Counter  # we will use this library to count the most occured label (vote)
import numpy as np

class K_Nearest_Nighbor:
    def __init__(self, k):
        self.k = k                  # k is the varible of the the nighor

    def cluster(self, X, y):        # to couple the train data with it's labels , there is no training in KNN
        self.X_train = X
        self.y_train = y

    def predict(self, X):           # to predict the label of the test data or any pic without label
        y_pred = [self.prediction(x) for x in X]  # here we loop through the entire data set , calculating distence of
        return np.array(y_pred)                     # of the single test data with each point in the data set

    def prediction(self, x):        # to calculate distence , sort the index, vote
        # Compute distances between x and all examples in the training set
        distances = [euc_dist(x, x_train) for x_train in self.X_train]
        # Sort by distance and return indices of the first k neighbors
        k_idx = np.argsort(distances)[: self.k]
        # Extract the labels of the k nearest neighbor training samples
        k_neighbor_labels = [self.y_train[i] for i in k_idx]
        # return the most common class label
        most_common = Counter(k_neighbor_labels).most_common(1)
        return most_common[0][0]

def euc_dist(x1, x2):
    return np.sqrt(np.sum((x1 - x2) ** 2))

