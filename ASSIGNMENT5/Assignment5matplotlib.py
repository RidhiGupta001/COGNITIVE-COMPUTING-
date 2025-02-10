import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(-10,10, num=100)
y = np.exp(x)
plt.plot(x,y, marker=".",color='g')
plt.title("Y = e^(X)")
plt.xlabel("X values")
plt.ylabel("Y values")
plt.grid()
plt.show()