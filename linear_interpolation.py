#bi aralıktaki noktalar arasında tahmin yapıp noktaları düz bi çizgi ile birleştirir

import numpy as np
import matplotlib.pyplot as plt

x_data = np.array([0, 1, 2, 3, 4])        #verilen noktalar
y_data = np.array([0, 1, 2, 3, 4])

x_estimate = float(input("Enter the x value between 0-4 to be estimated: "))  
if x_estimate < min(x_data) or x_estimate > max(x_data):
    print("ERROR:x value outside data range")
    exit()       #x in girilen değeri için y değeri bulucaz
 

linear = np.interp(x_estimate, x_data, y_data)     #2.5  2 ve 3 arasında olduğu için düz bir çizgi varmış gibi

print("Linear Interpolation")
print(f"Estimated x value : {x_estimate}")
print(f"Estimated y value: {linear:.6f}")

#çizgiyi çizmek için değer hesaplaması
x = np.linspace(min(x_data), max(x_data), 200)    #grafik düzgün çizilsin diye x değerleri üretiliyor
y = np.interp(x, x_data, y_data)

plt.scatter(x_data, y_data, label = "Original data points")     # noktalar çizilir
plt.plot(x, y, label = "Linear interpolation")                  # çizgi çizilir
plt.scatter(x_estimate, linear, label = "Estimated point")

plt.title("Linear Interpolation")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()      #açıklama kutusu
plt.grid(True)    #kareler
plt.show()