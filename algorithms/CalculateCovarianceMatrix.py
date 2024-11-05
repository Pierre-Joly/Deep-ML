def calculate_covariance_matrix(vectors: list[list[float]]) -> list[list[float]]:
    n, m = len(vectors), len(vectors[0])
    
    # Calculate means for each variable
    means = [sum(vectors[i]) / m for i in range(n)]
    
    # Initialize the covariance matrix
    covariance_matrix = [[0.0] * n for _ in range(n)]
    
    # Calculate covariance only for the lower triangle and the diagonal
    for i in range(n):
        for j in range(i + 1):
            covariance = sum((vectors[i][k] - means[i]) * (vectors[j][k] - means[j]) for k in range(m)) / (m - 1)
            covariance_matrix[i][j] = covariance
            if i != j:
                covariance_matrix[j][i] = covariance
    
    return covariance_matrix
