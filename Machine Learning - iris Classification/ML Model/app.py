'''
Classifying species of iris flowers using machine learning model which
basically looks at the neighbors of the inputed data number (specified in KNN)
and makes a prediction based on them
'''
import numpy as np
from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
IRIS = load_iris()

#x objects contain data to train and test while y contain target data (answers)
#random_state=0 makes it so the random split to train and test is going to be the same every time
X_TRAIN, X_TEST, Y_TRAIN, Y_TEST = train_test_split(IRIS['data'], IRIS['target'], random_state=0)
KNN = KNeighborsClassifier(n_neighbors=1)

#training, building model
KNN.fit(X_TRAIN, Y_TRAIN)

#ex data collected by botanist
X_NEW = np.array([[5.0, 2.9, 1.0, 0.2]])

#making a prediction
PREDICTION = KNN.predict(X_NEW)
print(IRIS.target_names[PREDICTION])

#caclulating accuracy
print("Accurracy: ~", KNN.score(X_TEST, Y_TEST) * 100, '%')
