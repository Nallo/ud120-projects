#!/usr/bin/python

"""
    This is the code to accompany the Lesson 3 (decision tree) mini-project.

    Use a Decision Tree to identify emails from the Enron corpus by author:
    Sara has label 0
    Chris has label 1
"""

import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###
from sklearn import tree

### Display the number of features.
print "Features:", len(features_train[0])

### Build the classifier.
clf = tree.DecisionTreeClassifier(min_samples_split=40)

### Fit the classifier with the training data.
clf = clf.fit(features_train, labels_train)

### Make the predictions.
pred = clf.predict(features_test)

### calculate and return the accuracy on the test data
from sklearn.metrics import accuracy_score
accuracy = accuracy_score(labels_test, pred)

### display the accuracy
print "Accuracy:", accuracy


#########################################################
