def matrixmul(a:list[list[int|float]],
              b:list[list[int|float]])-> list[list[int|float]]:
	num_rows_a, num_cols_a = len(a), len(a[0])
	num_rows_b, num_cols_b = len(b), len(b[0])

	if num_cols_a != num_rows_b:
		return -1

	result = [[0 for _ in range(num_cols_b)] for _ in range(num_rows_a)]

	for i in range(num_rows_a):
		for j in range(num_cols_b):
			result[i][j] = sum(a[i][k] * b[k][j] for k in range(num_cols_a))

	return result
