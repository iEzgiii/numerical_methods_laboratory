#eğriyi parabol gibi kullanıp daha hassas hesaplama yapar

import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.sin(x)

def integral(a, b):
    return -np.cos(b) + np.cos(a)

def simpson_rule(a, b, n):
    h = (b - a) / n

    x = np.linspace(a, b, n + 1)
    y = f(x)
    result = (h / 3) * (y[0] + y[n] + 4 * sum(y[1:n:2]) + 2 * sum(y[2:n - 1:2]))
    
    return result, x, y

a = float(input("\nEnter the lower limit(a):"))
b = float(input("Enter the upper limit(b):"))
n = int(input("Enter the number of subintervals(n):"))

if b <= a:
    print("\nERROR:Upper limit must be greater than lower limit.")
    exit()

if n <= 0:
    print("\nERROR:n must be greater than 0.")
    exit()

if n % 2 != 0:
    print("\nERROR:Simpson's rule requires an even number of subintervals.")
    exit()

simpson_result, x, y = simpson_rule(a, b, n)
result = integral(a, b)
error = abs(result - simpson_result)

print(f"\nLower limit: {a}")
print(f"Upper limit: {b}")
print(f"Number of subintervals: {n}")
print(f"Result: {simpson_result:.6f}")
print(f"Integral: {result:.6f}")
print(f"Error: {error:.6f}")

x_plot = np.linspace(a, b, 300)
y_plot = f(x_plot)
plt.plot(x_plot, y_plot, label = "f(x) = sin(x)")
plt.fill_between(x_plot, y_plot, alpha = 0.2, label = "Approximated Area")
plt.scatter(x, y, label = "Subinterval Points")

plt.title("Simpson's Rule")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.grid(True)
plt.show()