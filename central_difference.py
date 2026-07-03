#türev için hem sol hem sağ nokta kullanılır ve forward ile backwarda göre daha doğru sonuç verir

import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.sin(x)

def derivative(x):
    return np.cos(x)

def central_diff(x, h):
    return f(x + h) - f(x - h) / (2 * h)

x_value = float(input("\nEnter x value to calculate derivative: "))
h = float(input("Enter step size(h): "))

if h<= 0:
    print("ERROR:Step size must be bigger than 0.")
    exit()

central_result = central_diff(x_value, h)
result = derivative(x_value)
error = abs(result - central_result)

print(f"x value = {x_value}")
print(f"step size h: {h}")
print(f"Central difference result: {central_result:.6f}")
print(f"Derivative: {result:.6f}")
print(f"Absolute error: {error:.6f}")

x_plot = np.linspace(x_value - 2, x_value + 2, 500)
y_plot = f(x_plot)

x = np.array([x_value - h, x_value + h])
y = np.array([f(x_value - h), f(x_value + h)])

plt.plot(x_plot, y_plot, label = "f(x) = sin(x)")
plt.plot(x, y, linestyle = "--", label = "Central Difference Slope")
plt.scatter(x_value, f(x_value), color = "red", marker = "o", s = 80, label = "x", zorder = 5)
plt.scatter(x_value - h, f(x_value - h), color = "green", marker = "s", s = 80, label = "x - h", zorder = 5)
plt.scatter(x_value + h, f(x_value + h), color = "purple", marker = "^", s = 80, label = "x + h", zorder = 5)

plt.title("Central Difference")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.grid(True)
plt.show()
