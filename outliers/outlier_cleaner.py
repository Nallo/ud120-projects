#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where
        each tuple is of the form (age, net_worth, error).
    """

    cleaned_data = []

    ### Loop thorugh the data
    for idx in xrange(len(predictions)):
        pred = predictions[idx][0]
        net_worth = net_worths[idx][0]
        error = (pred - net_worth) ** 2
        cleaned_data.append((ages[idx][0], net_worth, error))

    return sorted(cleaned_data, key=lambda x: x[2])[:81]
