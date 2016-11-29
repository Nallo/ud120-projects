EVALUATION METRICS _Notes_
==========================

When runnig your machine learnign algorithm you may be interested in knowing
how accurate is in classifying your data. Here is where the **accuracy** comes really handy.

Accuracy is defined _tout court_ as:

```
            Number of all data points labeled correctly
Accuracy := -------------------------------------------
                    Number of all data points
```

However, accuracy has some shortcoming when:

  * Classed are skewed (denominator of the formula is a small number)
  * We want to min the error of misclassifying a data points

In some cases assigning a label to a data point can lead to serious consequences.
Think about an algorithm that classifies a person with cancer disease.
The accuracy of the cancer disease label _must_ be higher than _no cancer_ disease.

In this particular scenario, the **confusion matrix** plays a key role.

Confusion Matrix
================

The confusion matrix is a _2 x 2_ matrix which counts:

  * The number of _True Positive_ values.
  * The number of _False Positive_ values.
  * The number of _True Negative_ values.
  * The number of _False Negative_ values.
  
Here below is depicted a confusion matrix.


|                        | Class Positive | Class Negative  |
| ---------------------- | -------------- | --------------- |
| **Predicted Positive** | True Positives | False Positives |
| **Predicted Negative** | False Negative | True Negative   |

For instance, in an alarm system the number of _false positives_ must be really low.
Practically in a confusion matrix, **we want to make the major diagonal containing
the biggest values as possible.**

Recall
======

```
                        Number of True Positive
Recall := --------------------------------------------------
          Number of True Positive + Number of False Negative
```

Out of all the items that are truly positive, how many were correctly
classified as positive. Or simply, how many positive items were _recalled_
from the dataset.

Precision
=========

```
                        Number of True Positive
Precision := --------------------------------------------------
             Number of True Positive + Number of False Positive
```

Out of all the items labeled as positive, how many truly belong to the positive class.

F1-Score
========

```
                Precision * Recall
F1-Score := 2 * ------------------
                Precision + Recall
```

The _F1-Score_ is an evaluation metric that combine together _recall_ and _precision_.
See the [Wikipedia link](https://en.wikipedia.org/wiki/F1_score) for more information.
