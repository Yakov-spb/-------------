import numpy as np
import os
from matplotlib import pyplot as plt
a = 2
b = 1
plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True

def f(c):
   return c**a+c**b/c**b 
x = np.linspace(-10, 10, 1000)
plt.plot(x, f(x), color='red', linewidth=1)
plt.grid()
plt.show()