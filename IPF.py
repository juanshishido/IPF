import numpy as np
import os.path


def IPF(row_totals, col_totals, seed_values=None, random_fill=False):
    """
    Take two inputs: row and column totals.
    The inputs must be NumPy Arrays whose sums are equal.
    
    Optional input: seed_values (CSV only).

    Option: random_fill.
    """

    # Initial conditions
    assert type(row_totals) == np.ndarray
    assert type(col_totals) == np.ndarray
    assert sum(row_totals) == sum(col_totals)
    assert random_fill in (True, False)

    # Initialize the matrix
    if seed_values != None:
    	assert os.path.isfile(seed_values)
        matrix = np.loadtxt(seed_values, delimiter=',')
        assert matrix.shape[0] == len(row_totals)
        assert matrix.shape[1] == len(col_totals)
    elif seed_values == None:
        if random_fill == False:
            matrix = np.ones((len(row_totals), len(col_totals)))
        else:
            matrix = np.random.rand(len(row_totals),len(col_totals))

    # Row update
    row_scalars = matrix.sum(axis=1) / row_totals
    matrix = (matrix.T / row_scalars).T

    # Column update
    col_scalars = matrix.sum(axis=0) / col_totals
    matrix = (matrix / col_scalars)

    # Return
    return matrix