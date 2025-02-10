import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(-10,10, num=100)
y = x**2
plt.plot(x,y, marker=".")
plt.title("Y = X^2")
plt.xlabel("X values")
plt.ylabel("Y values")
plt.grid()
plt.show()