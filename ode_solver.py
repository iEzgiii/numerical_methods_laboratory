#değişimin hızını veren diferansiyel denklem ile sistemin zaman içerisinde davranışını hesaplar


import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

def decay_model(N, t, k):
    dNdt = -k * N
    return dNdt

def exact_solution(t, N0, k):
    return N0 * np.exp(-k * t)

N0 = float(input("\nEnter the initial value N0: "))
k = float(input("Enter the decay constant k: "))
final_time = float(input("Enter the final time: "))
num_points = int(input("Enter the number of time points: "))

if N0 <= 0:
    print("\nError: Initial value must be greater than zero.")
    exit()

if k <= 0:
    print("\nError: Decay constant must be greater than zero.")
    exit()

if final_time <= 0:
    print("\nError: Final time must be greater than zero.")
    exit()

if num_points <= 1:
    print("\nError: Number of time points must be greater than one.")
    exit()

t = np.linspace(0, final_time, num_points)

solution = odeint(decay_model, N0, t, args=(k,))

numerical_result = solution[:, 0]

exact_result = exact_solution(t, N0, k)

final_error = abs(exact_result[-1] - numerical_result[-1])

print("ODE model: dN/dt = -kN")
print(f"Initial value N0: {N0}")
print(f"Decay constant k: {k}")
print(f"Final time: {final_time}")
print(f"Number of time points: {num_points}")
print()
print(f"Numerical result at final time: {numerical_result[-1]:.6f}")
print(f"Exact result at final time: {exact_result[-1]:.6f}")
print(f"Absolute error at final time: {final_error:.6f}")
print()

plt.plot(t, numerical_result, label="Numerical Solution using odeint")
plt.plot(t, exact_result, linestyle="--", label="Exact Solution")

plt.title("ODE Solver: Exponential Decay")
plt.xlabel("Time")
plt.ylabel("N(t)")
plt.legend()
plt.grid(True)
plt.show()