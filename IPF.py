import numpy as numpy


def IPF(row_totals, col_totals):
	"""
	Take two inputs: row and column totals.
	The inputs must be NumPy Arrays whose sums are equal.
	"""

	# Conditions
	assert type(row_totals) == np.ndarray
	assert type(col_totals) == np.ndarray
	assert sum(row_totals) == sum(col_totals)

	# Initialize the matrix with 1s
	matrix = np.ones((len(row_totals), len(col_totals)))

	# Row update
	row_scalars = matrix.sum(axis=1) / row_vals
	matrix = (matrix.T / row_scalars).T

	# Column update
	col_scalars = matrix.sum(axis=0) / col_vals
	matrix = (matrix / col_scalars)

	# Return
	return matrix
