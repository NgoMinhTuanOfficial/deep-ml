import numpy as np
def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	axis = 0
	if mode == 'row':
		axis = 1
		
	return np.mean(np.array(matrix), axis=axis).tolist()