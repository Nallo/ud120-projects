#!/usr/bin/python


"""
    Starter code for the validation mini-project.
    The first step toward building your POI identifier!

    Start by loading/formatting the data

    After that, it's not our code anymore--it's yours!
"""

import pickle
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r") )

### first element is our labels, any added elements are predictor
### features. Keep this the same for the mini-project, but you'll
### have a different feature list when you do the final project.
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)



### 1. Create a decision tree with default parameters.
from sklearn import tree
clf = tree.DecisionTreeClassifier()

### 2. Fit the decision tree on the whole dataset.
clf.fit(features, labels)

### 3. Compute the decision tree's score on the training set
###    should lead to a score close to 100%.
print 'overfitted decision tree score: %.2f' % clf.score(features, labels)

### 4. Split the input data into trainig (70%) and test (30%).
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.3, random_state=42)

### 5. Print training / test set sizes.
print 'Dataset size     ', len(features), '(100%)'
print 'Test set size    ', len(X_test),   '(30%)'
print 'Training set size', len(X_train),  '(70%)'

### 6. Create another decision tree with default parameters to use on trainig set.
clf2 = tree.DecisionTreeClassifier()

### 7. Fit the decision tree on the training set.
clf2.fit(X_train, y_train)

### 8. Compute the decision tree's score.
print 'splitted decision tree score: %.2f' % clf2.score(X_test, y_test)
