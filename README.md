# IPF
Iterative Proportional Fitting in Python

## What It Does
IPF fills in a matrix given row and column totals whose respective sums are equal.

## How It Works
The algorithm fills the matrix with either all 1s or random numbers to start. These are the seed values. Then, each row in the matrix is scaled so that it sums to its respective row total. The same update is done to each column. This is repeated until additional updates have little effect, as defined by the user, on the values.

It's important to note that the results don't necessarily yield true values and that they depend on the seed values.

## Use Cases
Sometimes, publicly available data is provided at a level without enough granularity. IPF provides a set of values that fit within the row and column total constraints.
