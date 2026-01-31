import numpy as np

def euclidean_distance(x, y):
    """
    Compute the Euclidean (L2) distance between vectors x and y.
    Must return a float.
    """
    # Write code here
    arr1 = np.asarray(x ,dtype=float)
    arr2 = np.asarray(y ,dtype=float)

    dif = arr1 - arr2
    sqr = dif ** 2
    sumTotal = np.sum(sqr)
    dist = np.sqrt(sumTotal)
    return dist