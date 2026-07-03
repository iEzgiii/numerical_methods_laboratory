#Ax = b şeklinde olan lineer sistemleri çözüp bilinmeyenleri bulurr

import numpy as np
np.set_printoptions(precision=4, suppress=True)

n = int(input("Enter the number of equations: "))

A = np.zeros((n, n))
b = np.zeros(n)

print("Enter the coefficients of matrix A:")

for i in range(n):
    for j in range(n):
        A[i][j] = float(input(f"A[{i + 1}][{j + 1}]: "))

print("Enter the constants of vector b:")

for i in range(n):
    b[i] = float(input(f"b[{i + 1}]: "))

det_A = np.linalg.det(A)

if abs(det_A) < 1e-10:
    print("Error: The system has no unique solution because determinant is zero.")
    exit()

solution = np.linalg.solve(A, b)

check = np.dot(A, solution)

error = np.abs(check - b)

print("\nCoefficient matrix(A):")
print(A)

print("\nConstant vector(b):")
print(b)

print("\nSolution vector(x):")
print(solution)

print("\nCheck Ax:")
print(check)

print("\nAbsolute error:")
print(error)
print()