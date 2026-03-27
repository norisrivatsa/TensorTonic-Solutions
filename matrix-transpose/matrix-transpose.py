import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    # Write code here
    arr = np.array(A)
    shape = arr.shape
    rows_n = shape[0]
    print(rows_n)
    trans_arr = np.empty((shape[1],shape[0]))
    for i in range(shape[0]):
        for j in range(shape[1]):
            trans_arr[j][i] = arr[i][j]

    return trans_arr