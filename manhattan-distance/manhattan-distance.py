import numpy as np

def manhattan_distance(x, y):
    """
    Compute the Manhattan (L1) distance between vectors x and y.
    Must return a float.
    """
    arr1 = np.array(x)
    arr2 = np.array(y)
    arr3 = arr1 - arr2
    arr4 = np.abs(arr3)
    sum = np.sum(arr4)
    return int(sum)