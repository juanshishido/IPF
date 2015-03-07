import numpy as numpy


def IPF(row_totals, col_totals, random_fill=False):
	"""
	Take two inputs: row and column totals.
	The inputs must be NumPy Arrays whose sums are equal.
	"""

	# Conditions
	assert type(row_totals) == np.ndarray
	assert type(col_totals) == np.ndarray
	assert sum(row_totals) == sum(col_totals)
	assert random_fill in (True, False)

	# Initialize the matrix
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