#eğrinin altında küçük yamuklarla yaklaşık integral

import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.sin(x)

def integral(a, b):
    return -np.cos(b) + np.cos(a)

def trapezoidal(a, b, n):
    h = (b - a) / n
    
    x = np.linspace(a, b, n + 1)
    y = f(x)
    result = (h / 2) * (y[0] + 2 * sum(y[1:n]) + y[n])
    return result, x, y

a = float(input("Enter the lower limit(a): "))
b = float(input("Enter the upper limit(b): "))
n = int(input("Enter the numbre of subintervals(n): "))

if b <= a:
    print("ERROR:Upper limit must be greater than lower limit.")
    exit()

if n <= 0:
    print("ERROR:Number of subintervals must be greater than 0.")
    exit()

trapezoidal_result, x, y = trapezoidal(a, b, n)
result = integral(a, b)
error = abs(result - trapezoidal_result)

print(f"\nLower limit: {a}")
print(f"Upper limiy: {b}")
print(f"Number of subintervals: {n}")
print(f"Result: {trapezoidal_result:.6f}")
print(f"Integral: {result:.6f}")
print(f"Absolute error: {error:.6f}")

x_plot = np.linspace(a, b, 300)
y_plot = f(x_plot)
plt.plot(x_plot, y_plot, label = "f(x) = sin(x)")
plt.plot(x, y, marker = "o", label = "Trapezoids")

for i in range (n):
    x_trap = [x[i], x[i], x[i + 1], x[i + 1]]
    y_trap = [0, y[i], y[i + 1], 0]
    plt.fill(x_trap, y_trap, alpha = 0.2)

plt.title("Trapezoidal Rule")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.grid(True)
plt.show()