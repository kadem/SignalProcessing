
import pandas as pd
import scipy.io
from sklearn.ensemble import RandomForestClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn import metrics

def initialize():
    data = pd.read_csv("C:/Users/Kamil Adem/Downloads/CS484-master/CS484-master/train_features.txt", sep =",", header = None)
    test = pd.read_csv("C:/Users/Kamil Adem/Downloads/CS484-master/CS484-master/test_features.txt", sep = ",", header = None)

    X_train = data.values[:,0:7]
    y_train = data.values[: ,7]
    X_test = test.values[:,0:7]
    y_test = test.values[:, 7]
    
    return X_train, y_train, X_test, y_test, mat

def RandomForest(X_train, y_train, X_test, y_test):
    rf = RandomForestClassifier(n_estimators = 10000, max_depth = 10)
    rf.fit(X_train, y_train)
    y_predict = rf.predict(X_test)
    
    print("RandomForest:")
    print("Accuracy on training ", format(rf.score(X_train, y_train)*100))
    print("Accuracy on testing ", format(rf.score(X_test, y_test)*100))
    print("Accuracy is ", format(metrics.accuracy_score(y_test, y_predict)*100))
    print("")
    return y_predict

def NeuralNetwork(X_train, y_train, X_test, y_test):
    nn = MLPClassifier(max_iter = 1000, activation = 'logistic')
    nn.fit(X_train, y_train)
    y_predict = nn.predict(X_test)
    
    print("NeuralNetwork:")
    print("Accuracy on training ", format(nn.score(X_train, y_train)*100))
    print("Accuracy on testing ", format(nn.score(X_test, y_test)*100))
    print("Accuracy is ", format(metrics.accuracy_score(y_test, y_predict)*100))
    print("")
    return y_predict

def NearestNeighbor(X_train, y_train, X_test, y_test):
    neigh = KNeighborsClassifier(n_neighbors=4)
    neigh.fit(X_train, y_train)
    y_predict = neigh.predict(X_test)
    
    print("NearestNeighbor:")
    print("Accuracy on training ", format(neigh.score(X_train, y_train)*100))
    print("Accuracy on testing ", format(neigh.score(X_test, y_test)*100))
    print("Accuracy is ", format(metrics.accuracy_score(y_test, y_predict)*100))
    print("")
    return y_predict

def NaiveBayes(X_train, y_train, X_test, y_test):
    nb = GaussianNB()
    nb.fit(X_train, y_train)
    y_predict = nb.predict(X_test)
    
    print("NaiveBayes:")
    print("Accuracy on training ", format(nb.score(X_train, y_train)*100))
    print("Accuracy on testing ", format(nb.score(X_test, y_test)*100))
    print("Accuracy is ", format(metrics.accuracy_score(y_test, y_predict)*100))
    print("")
    return y_predict

def SupportVector(X_train, y_train, X_test, y_test):
    sv = SVC()
    sv.fit(X_train, y_train)
    y_predict = sv.predict(X_test)
    
    print("Support Vector:")
    print("Accuracy on training ", format(sv.score(X_train, y_train)*100))
    print("Accuracy on testing ", format(sv.score(X_test, y_test)*100))
    print("Accuracy is ", format(metrics.accuracy_score(y_test, y_predict)*100))
    return y_predict

X_train, y_train, X_test, y_test, mat= initialize()
RandomForest(X_train, y_train, X_test, y_test)
NeuralNetwork(X_train, y_train, X_test, y_test)
NearestNeighbor(X_train, y_train, X_test, y_test)
NaiveBayes(X_train, y_train, X_test, y_test)
SupportVector(X_train, y_train, X_test, y_test)