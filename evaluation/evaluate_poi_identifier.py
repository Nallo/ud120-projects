#!/usr/bin/python


"""
    Starter code for the evaluation mini-project.
    Start by copying your trained/tested POI identifier from
    that which you built in the validation mini-project.

    This is the second step toward building your POI identifier!

    Start by loading/formatting the data...
"""

import pickle
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r") )

### add more features to features_list!
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)



### The same code as validation mini-project
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.3, random_state=42)

### Print training / test set sizes.
print 'Dataset size     ', len(features), '(100%)'
print 'Test set size    ', len(X_test),   '(30%)'
print 'Training set size', len(X_train),  '(70%)'

### Create a decision tree with default parameters to use on trainig set.
from sklearn import tree
clf = tree.DecisionTreeClassifier()

### Fit the decision tree on the training set.
clf.fit(X_train, y_train)

### Compute the decision tree's score (0.724).
print 'cross-validated decision tree score: %.3f' % clf.score(X_test, y_test)

### 1. Metrics on test set.
import numpy as np
print 'POIs in the test set:        ', np.count_nonzero(y_test)
print 'People in the test set:      ', len(y_test)

### 2. Run the model on the test input data.
pred = clf.predict(X_test)
print 'POIs identified by the model:', np.count_nonzero(pred)

### 3. Precision and Recall metrics.
from sklearn.metrics import recall_score
from sklearn.metrics import precision_score
print 'Model Recall metric:         ', recall_score(y_test, pred)
print 'Model Precision metric:      ', precision_score(y_test, pred)

### 4. Custom data.
predictions = [0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1]
true_labels = [0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0]

### 5. TP, TN, FP, FN.
tp = tn = fp = fn = 0
for idx in range(len(true_labels)):
    if true_labels[idx]==1 and true_labels[idx]==predictions[idx]:
        tp += 1
    if true_labels[idx]==0 and true_labels[idx]==predictions[idx]:
        tn += 1
    if predictions[idx]==1 and true_labels[idx]!=predictions[idx]:
        fp += 1
    if predictions[idx]==0 and true_labels[idx]!=predictions[idx]:
        fn += 1

print 'True Positives: ', tp
print 'True Negatives: ', tn
print 'False Positives:', fp
print 'False Negatives:', fn
print 'Recall:    %.3f' % (float(tp)/float(tp + fn))
print 'Precision: %.3f' % (float(tp)/float(tp + fp))
