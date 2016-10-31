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

    ### We need to cut the data size to a 90%
    data_size = len(predictions)
    reduced_data_size = int(data_size * 0.9)

    for idx in xrange(data_size):
        pred = predictions[idx][0]
        net_worth = net_worths[idx][0]
        error = (pred - net_worth) ** 2
        cleaned_data.append((ages[idx][0], net_worth, error))

    return sorted(cleaned_data, key=lambda x: x[2])[:reduced_data_size]
