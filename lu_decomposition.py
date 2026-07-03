#kullanıcıdan alınan matrisi alt üçgensel ve üst üçgensel olarak ikiye ayırıp çarpımları asıl matrise eşit mi bakar

import numpy as np
np.set_printoptions(precision=4, suppress=True)

n = int(input("Enter the size of the square matrix: "))

A = np.zeros((n, n))

print("Enter the elements of matrix A:")

for i in range(n):
    for j in range(n):
        A[i][j] = float(input(f"A[{i + 1}][{j + 1}]: "))

L = np.zeros((n, n))
U = np.zeros((n, n))

for i in range(n):
    L[i][i] = 1

for i in range(n):

    for j in range(i, n):
        total = 0
        for k in range(i):
            total += L[i][k] * U[k][j]

        U[i][j] = A[i][j] - total

    if abs(U[i][i]) < 1e-10:
        print("Error: LU decomposition cannot continue because pivot is zero.")
        exit()

    for j in range(i + 1, n):
        total = 0
        for k in range(i):
            total += L[j][k] * U[k][i]

        L[j][i] = (A[j][i] - total) / U[i][i]

check = np.dot(L, U)

error = np.abs(A - check)

print("\nOriginal matrix(A):")
print(A)

print("\nLower triangular matrix(L):")
print(L)

print("\nUpper triangular matrix(U):")
print(U)

print("\nCheck L * U:")
print(check)

print("\nAbsolute error:")
print(error)

print()