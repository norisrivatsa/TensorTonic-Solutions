import numpy as np

def sigmoid(x):
    """
    Vectorized sigmoid function.
    """
    # Write code here
    array = np.asarray(x ,dtype=float)
    
    neg = np.negative(array)
    exp = np.exp(neg)
    plus = exp + 1
    div = 1 / plus
    return div
    