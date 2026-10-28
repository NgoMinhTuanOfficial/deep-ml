import numpy as np

def make_diagonal(x):
	result = np.eye(len(x))
	for i in range(len(x)):
		result[i][i] = x[i]
	return result