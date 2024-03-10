import matplotlib.pyplot as plt
import numpy as np
from numpy import cos

x = np.linspace(0,2.180,1000000) #Return evenly spaced numbers over a specified interval
y = (0.5 * x ** 2) * cos(x ** 2)
plt.plot(x, y, 'r-')
plt.title("Graph")
plt.grid(True, color = "grey", linestyle = "-.")
plt.show()

roots = []
for i in range(len(y)-1):
    if y[i] == 0:
        roots.append(x[i])
    elif y[i] < 0 < y[i + 1] or y[i] > 0 > y[i + 1]:
        roots.append(x[i])
print(f"roots of the function: {roots}")

lenght = []
for i in range(len(y) - 1):
     l = np.sqrt(np.square(x[i] - x[i + 1]) + np.square(y[i] - y[i + 1]))
     lenght.append(l)
print(f"lenght of the way: {np.sum(lenght)*2}")