
import pandas as pd
import scipy.io
from sklearn.ensemble import RandomForestClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn.model_selection import KFold

def initialize():
    data = pd.read_csv("final_features.txt", sep =",", header = None)
    
    X = data.values[:, 0:11]
    y = data.values[:, 11]

    kf = KFold(n_splits=10, random_state=17, shuffle=True)
    kf.get_n_splits(X)
    for train_index, test_index in kf.split(X):
       X_train, X_test = X[train_index], X[test_index]
       y_train, y_test = y[train_index], y[test_index]
       #RandomForest(X_train, y_train, X_test, y_test)
       #NeuralNetwork(X_train, y_train, X_test, y_test)
       #NearestNeighbor(X_train, y_train, X_test, y_test)
       #NaiveBayes(X_train, y_train, X_test, y_test)
       SupportVector(X_train, y_train, X_test, y_test)
    
    #X_train, X_test, y_train, y_test = train_test_split(X, y, random_state = 0)
    #return X_train, y_train, X_test, y_test

def RandomForest(X_train, y_train, X_test, y_test):
    rf = RandomForestClassifier(n_estimators = 10000, max_depth = 10, random_state = 17)
    rf.fit(X_train, y_train)
    y_predict = rf.predict(X_test)
    
    print("RandomForest:")
    print("Accuracy on training ", format(rf.score(X_train, y_train)*100))
    print("Accuracy on testing ", format(rf.score(X_test, y_test)*100))
    print("Accuracy is ", format(metrics.accuracy_score(y_test, y_predict)*100))
    print("")
    return y_predict

def NeuralNetwork(X_train, y_train, X_test, y_test):
    nn = MLPClassifier(hidden_layer_sizes = (100,100),max_iter = 1000, activation = 'logistic', solver = 'lbfgs', random_state = 17)
    nn.fit(X_train, y_train)
    y_predict = nn.predict(X_test)
    
    print("NeuralNetwork:")
    print("Accuracy on training ", format(nn.score(X_train, y_train)*100))
    print("Accuracy on testing ", format(nn.score(X_test, y_test)*100))
    print("Accuracy is ", format(metrics.accuracy_score(y_test, y_predict)*100))
    print("")
    return y_predict

def NearestNeighbor(X_train, y_train, X_test, y_test):
    neigh = KNeighborsClassifier(n_neighbors=10)
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
    sv = SVC(kernel='poly')
    sv.fit(X_train, y_train)
    y_predict = sv.predict(X_test)
    
    print("Support Vector:")
    print("Accuracy on training ", format(sv.score(X_train, y_train)*100))
    print("Accuracy on testing ", format(sv.score(X_test, y_test)*100))
    print("Accuracy is ", format(metrics.accuracy_score(y_test, y_predict)*100))
    return y_predict

#X_train, y_train, X_test, y_test= initialize()
initialize()
#RandomForest(X_train, y_train, X_test, y_test)
#NeuralNetwork(X_train, y_train, X_test, y_test)
#NearestNeighbor(X_train, y_train, X_test, y_test)
#NaiveBayes(X_train, y_train, X_test, y_test)
#SupportVector(X_train, y_train, X_test, y_test)