def calculate_eigenvalues(matrix):
    a, b = matrix[0]
    c, d = matrix[1]

    # Coefficients for the quadratic equation Ax^2 + Bx + C = 0
    A = 1
    B = -(a + d)
    C = (a * d) - (b * c)

    # Calculate the discriminant
    discriminant = B**2 - 4 * A * C

    # Calculate the two roots using the quadratic formula
    if discriminant < 0:
        # Complex eigenvalues, return them in a complex form
        real_part = -B / (2 * A)
        imaginary_part = (abs(discriminant)**0.5) / (2 * A)
        eigen1 = complex(real_part, imaginary_part)
        eigen2 = complex(real_part, -imaginary_part)
    else:
        # Real eigenvalues
        sqrt_discriminant = discriminant**0.5
        eigen1 = (-B + sqrt_discriminant) / (2 * A)
        eigen2 = (-B - sqrt_discriminant) / (2 * A)

    return sorted([eigen1, eigen2], reverse=True)