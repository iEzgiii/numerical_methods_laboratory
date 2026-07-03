#fonksiyonun türevinin yaklaşık değerini bulmak için x ve x - h kullanır

import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.sin(x)

def exact_derivative(x):
    return np.cos(x)

def backward_diff(x, h):
    return (f(x) - f(x - h)) / h

x_value = float(input("\nEnter the x value to calculate derivative: "))
h = float(input("Enter the step size(h): "))

if h<= 0:
    print("ERROR:Step size must be greater than 0.")
    exit()

backward_result = backward_diff(x_value, h)
exact_result = exact_derivative(x_value)
error = abs(exact_result - backward_result)

print(f"\nx value: {x_value}")
print(f"Step size: {h}")
print(f"Backward difference result: {backward_result:.6f}")
print(f"Exact derivative: {exact_result:.6f}")
print(f"Absolute error: {error:.6f}")

x_plot = np.linspace(x_value -2, x_value + 2, 500)
y_plot = f(x_plot)

x = np.array([x_value - h, x_value])
y = np.array([f(x_value - h), f(x_value)])

plt.plot(x_plot, y_plot, label = "f(x) = sin(x)")
plt.plot(x, y, linestyle = "--", label = "Backward Difference Slope")
plt.scatter(x_value, f(x_value), color = "red", marker = "o", s = 80, label = "x", zorder = 5)
plt.scatter(x_value - h, f(x_value - h), color = "green",  marker = "s", s = 80, label = "x - h", zorder = 5)
plt.title("Backward Difference")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.grid(True)
plt.show()