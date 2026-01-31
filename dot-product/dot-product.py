import numpy as np

def dot_product(x, y):
    """
    Compute the dot product of two 1D arrays x and y.
    Must return a float.
    """
    # Write code here
    arr1 = np.asarray(x, dtype=float)
    arr2 = np.asarray(y, dtype=float)

    prod = arr1 * arr2
    dotsum = np.sum(prod)

    return dotsum