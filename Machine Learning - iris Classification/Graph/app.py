'''
Classifying species of iris flowers using mchine learning model
'''
import matplotlib.pyplot as plt

from sklearn.datasets import load_iris
IRIS = load_iris()

FEATURES = IRIS.data.T

SEPAL_LENGTH, SEPAL_WIDTH = FEATURES[0], FEATURES[1]
PETAL_LENGTH, PETAL_WIDTH = FEATURES[2], FEATURES[3]

SEPAL_LENGTH_LABEL, SEPAL_WIDTH_LABEL = IRIS.feature_names[0], IRIS.feature_names[1]
PETAL_LENGTH_LABEL, PETAL_WIDTH_LABEL = IRIS.feature_names[2], IRIS.feature_names[3]

plt.scatter(SEPAL_LENGTH, SEPAL_WIDTH, c=IRIS.target)
plt.xlabel(SEPAL_LENGTH_LABEL)
plt.ylabel(SEPAL_WIDTH_LABEL)
plt.show()
