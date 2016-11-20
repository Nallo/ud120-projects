Principal Component Analysis - PCA _Notes_
==========================================

PCA is a powerful technique to use when we want to combine together two or more
features into a single one. In particular, if the two features are correlated,
the PCA transforms such features into a new set of linearly uncorrelated features.

Imagine we get a dataset to predict house prices given their sizes and, for
each sample, among several other features, we have:

* the number of rooms
* the stepping area

We want to combine these two features into a single feature called **size**.

In this particular scenario PCA becomes really handy.

What PCA practically does?
==========================

Given a set of features in a reference system _(X,Y)_, PCA executes a rigid
transformation to the feature axis (translation + rotation) so to generate a new
reference system _(X', Y')_ where:

* X' is the axis where we have the _max_ variance of the data.
* Y' is the axis where we have the _second-max_ variance of the data and is
  perpendicular to X'.
* The _k-th_ axis has the _k-th-max_ variance and is perpendicular to the former
  _k-1_ axis.

PCA gotcha
==========

* PCA is a way to transform input features into Principal Components - PCs.
* When using PCA it is highly recommended to use the Principal Components as new
  features.
* PCs are direction in data where the variance is maximized when projecting the
  data to the PC.
* The first PC is the direction where data has the maximum variance.
* The second PC is the direction where data has the second-maximum variance.
* All the PCs are perpendicular among themselves therefore, it is safe to use
  them as independent feature.
* The maximum number of PCs is the number of input features.
* ***Do not*** do feature selection **before** PCA.

PCA in Sklearn
==============

    ### 1. import RandomizedPCA.
    from sklearn.decomposition import RandomizedPCA

    ### 2. Instantiace the PCA object and fit it to the training data.
    pca = RandomizedPCA(n_components=2).fit(X_train)

    ### 3. Transform the input data after running PCA.
    X_train_pca = pca.transform(X_train)
    X_test_pca = pca.transform(X_test)

    ### 4. Display the variance of the max and the second-max PCs.
    print "variance of the first PC %f" % pca.explained_variance_ratio_[0]
    print "variance of the second PC %f" % pca.explained_variance_ratio_[1]
