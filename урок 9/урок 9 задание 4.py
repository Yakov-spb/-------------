import numpy as np
from matplotlib import pyplot as plt
import pylab
d=0
x_left = np.linspace(-2, d - 0.08, 2000)  # Левее точки разрыва
x_right = np.linspace( d + 0.08, 2, 2000)

# График  2
a = 1
b = 0.5
pylab.subplot (1, 6, 1)
def f(x):
    return (x**b+a**b)/x**b

#plt.figure(figsize=(8, 6))генерация нового окна и его параметры
plt.plot(x_left, f(x_left), label=r"$f(x) = \frac{x^{b}+a^{b}}{x^{b}}$", color="blue")
plt.plot(x_right, f(x_right), color="green")
plt.ylim(0,5)
plt.ylabel("f(x)")
plt.grid()




# График  3
a = 1
b = 0.8
pylab.subplot (1, 6, 2)
def f(x):
    return (x**b+a**b)/x**b



plt.plot(x_right, f(x_right), color="green")
plt.plot(x_left, f(x_left), color="blue")
# настройки
plt.ylim(0,5)
plt.grid()
plt.ylabel("f(x)")
plt.title("График функции с точкой разрыва второго рода")


a = 1
b = 0.5
pylab.subplot (1, 6, 3)
def f(x):
    return (x**b+a**b)/x**b

#plt.figure(figsize=(8, 6))генерация нового окна и его параметры
plt.plot(x_left, f(x_left), label=r"$f(x) = \frac{x^{b}+a^{b}}{x^{b}}$", color="blue")
plt.plot(x_right, f(x_right), color="green")
plt.ylim(0,5)
plt.ylabel("f(x)")
plt.grid()

a = 1
b = -0.5
pylab.subplot (1, 6, 4)
def f(x):
    return (x**b+a**b)/x**b

#plt.figure(figsize=(8, 6))генерация нового окна и его параметры
plt.plot(x_left, f(x_left), label=r"$f(x) = \frac{x^{b}+a^{b}}{x^{b}}$", color="blue")
plt.plot(x_right, f(x_right), color="green")
plt.ylim(0,5)
plt.ylabel("f(x)")
plt.grid()

a = 1
b = -1.5
pylab.subplot (1, 6, 5)
def f(x):
    return (x**b+a**b)/x**b

#plt.figure(figsize=(8, 6))генерация нового окна и его параметры
plt.plot(x_left, f(x_left), label=r"$f(x) = \frac{x^{b}+a^{b}}{x^{b}}$", color="blue")
plt.plot(x_right, f(x_right), color="green")
plt.ylim(0,5)
plt.ylabel("f(x)")
plt.grid()

a = 1
b = -2.5
pylab.subplot (1, 6, 6)
def f(x):
    return (x**b+a**b)/x**b

#plt.figure(figsize=(8, 6))генерация нового окна и его параметры
plt.plot(x_left, f(x_left), label=r"$f(x) = \frac{x^{b}+a^{b}}{x^{b}}$", color="blue")
plt.plot(x_right, f(x_right), color="green")
plt.ylim(0,5)
plt.ylabel("f(x)")
plt.grid()


plt.legend()
plt.show()

