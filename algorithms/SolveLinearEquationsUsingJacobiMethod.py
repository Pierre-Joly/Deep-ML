import numpy as np
def solve_jacobi(A: np.ndarray, b: np.ndarray, n: int) -> list:
	x = np.zeros(len(b))
	diagonal = np.diag(A)
	off_diagonal = A - np.diag(diagonal)
	for i in range(n):
		x = np.divide((b - off_diagonal @ x), diagonal)
	return x.tolist()