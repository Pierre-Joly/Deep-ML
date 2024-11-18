def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	n, m = len(matrix), len(matrix[0])
	if mode == 'row':
		means = [sum(matrix[i])/m for i in range(n)]
	elif mode == 'column':
		means = [sum([matrix[i][j] for i in range(n)])/n for j in range(m)]
	return means