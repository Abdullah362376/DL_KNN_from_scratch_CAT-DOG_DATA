# file NO# 5
# in this code we test the KNN algo , we import from the KNN class we made in file NO#4
# we also defined an accuracy function to test the accuracy of our algo

from KNN import *                   # import everything in KNN.py
def accuracy(y_true, y_pred):       # simple functionn to compute accuracy
    accuracy = np.sum(y_true == y_pred) / len(y_true)
    return accuracy

X = np.load("data_set.npy")  # load the data set
Y = np.load("labels.npy")    # load the label set
X_test = np.load("test_set.npy")    # load the test data
y_test = np.load("test_labels.npy")     # load the label of the test data


k = 2    # number of the nighbors to be chosen
clus = K_Nearest_Nighbor(k=k)  # call the class from KNN
clus.cluster(X, Y)       # call the clustering functionn
predictions = clus.predict(X_test)  # call the predect function

print("KNN classification accuracy", accuracy(y_test, predictions))

