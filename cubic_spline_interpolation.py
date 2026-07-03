#bi aralıktaki noktalar arasında tahmin yapıp noktaları daha yumuşak şekilde birleştirir

import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline

x_data = np.array([0, 1, 2, 3, 4])
y_data = np.array([0, 2, 3, 5, 4])

x_estimate = float(input("Enter the x value between 0-4 to be estimated: "))
if x_estimate < min(x_data) or x_estimate > max(x_data):
    print("ERROR:x value outside data range")
    exit()

cubic_spline = CubicSpline(x_data, y_data)
cubic_value = cubic_spline(x_estimate)

print("\nCubic spline interpolation")
print(f"Estimated x: {x_estimate}")
print(f"Estimate y: {cubic_value:.6f}")

x = np.linspace(min(x_data), max(x_data), 200)
y = cubic_spline(x)

plt.scatter(x_data, y_data, label= "Original data")
plt.plot(x, y, label = "Cubic Spline Interpolation")
plt.scatter(x_estimate, cubic_value, label = "Estimated point")

plt.title("Cubic Spline Interpolation")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.show()