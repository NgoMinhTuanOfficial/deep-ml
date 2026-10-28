
import numpy as np

def matrix_image(A):
	A_float = A.astype(float)
	m, n = A_float.shape
	pivot_cols = []
	current_row = 0
	esp = 1e-9
	for col in range(n):
		if current_row >= m:
			break

		max_row = current_row + np.argmax(np.abs(A_float[current_row:, col]))

		if np.abs(A_float[max_row, col]) < esp:
			continue
		A_float[[current_row, max_row]] = A_float[[max_row, current_row]]

		pivot_cols.append(col)
		pivot_val = A_float[current_row, col]
		for r in range(current_row + 1, m):
			factor = A_float[r, col]/pivot_val
			A_float[r, col:] -= factor*A_float[current_row, col:]

		current_row += 1
	return A[:, pivot_cols]

