import numpy as np

def linear_regression_gradient_descent(X: np.ndarray, y: np.ndarray, alpha: float, iterations: int) -> np.ndarray:
    m, n = X.shape
    theta = np.zeros((n, 1))
    y = y.reshape(-1, 1)
    learning_rate = alpha / m

    for i in range(iterations):
        gradient = X.T @ (X @ theta - y)
        theta = theta - learning_rate * gradient

    return theta.flatten()
