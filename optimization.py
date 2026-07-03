# minimize scalar    tek değişkenli fonksiyonda verilen aralık içindeki minimum değeri hesplar

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize_scalar

def function(x):
    return (x - 3)**2 + 5

lower_bound = float(input("\nEnter the lower bound: "))
upper_bound = float(input("Enter the upper bound: "))

if upper_bound <= lower_bound:
    print("\nError: Upper bound must be greater than lower bound.")
    exit()

result = minimize_scalar(
    function,
    bounds=(lower_bound, upper_bound),
    method="bounded"
)

print("\nFunction: f(x) = (x - 3)^2 + 5")
print(f"Search interval: [{lower_bound}, {upper_bound}]")
print(f"Minimum x value: {result.x:.6f}")
print(f"Minimum function value: {result.fun:.6f}")
print(f"Optimization success: {result.success}")
print(f"Number of function evaluations: {result.nfev}")
print(f"Message: {result.message}")
print()

x_plot = np.linspace(lower_bound - 2, upper_bound + 2, 300)
y_plot = function(x_plot)

plt.plot(x_plot, y_plot, label="f(x) = (x - 3)^2 + 5")
plt.scatter(result.x, result.fun, color="red", s=80, label="Minimum")

plt.axvspan(lower_bound, upper_bound, alpha=0.2, label="Search Interval")

plt.title("Scalar Optimization using minimize_scalar")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.grid(True)
plt.show()