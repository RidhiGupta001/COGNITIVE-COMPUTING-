import numpy as np
from matplotlib import pyplot as plt
x = np.linspace(-10,10, num=100)
y = x**2
y = np.sin(x)
plt.plot(x,y, marker=".", color='r')
plt.title("Y = sin(X)")
plt.xlabel("X values")
plt.ylabel("Y values")
plt.grid()
plt.show()