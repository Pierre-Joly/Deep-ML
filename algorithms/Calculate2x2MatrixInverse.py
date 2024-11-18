def inverse_2x2(matrix):
    a, b = matrix[0]
    c, d = matrix[1]

    # Calculate the determinant
    determinant = a * d - b * c

    # Check if the matrix is invertible
    if determinant == 0:
        return None  # Matrix is not invertible

    # Compute the inverse using the formula for 2x2 matrices
    inverse = [
        [d / determinant, -b / determinant],
        [-c / determinant, a / determinant]
    ]

    return inverse