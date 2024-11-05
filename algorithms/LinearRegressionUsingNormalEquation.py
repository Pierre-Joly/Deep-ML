import numpy as np

def linear_regression_normal_equation(X: list[list[float]], y: list[float]) -> list[float]:
	X = np.array(X)
	Y = np.array(y)
	theta = np.linalg.solve(X.T @ X, X.T @ Y)
	return np.round(theta, 4).tolist()
