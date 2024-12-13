
#точка разрыва
d = 0
w=0
import numpy as np
from matplotlib import pyplot as plt
x_left = np.linspace(-2, d - 0.08, 2000)  # Левее точки разрыва
x_right = np.linspace( d + 0.08, 2, 2000)


#график 1
a = 2
b = 1
def f(x):
    return (x**b+a**b)/x**b

#plt.figure(figsize=(8, 6))
plt.plot(x_left, f(x_left), label=r"$f(x) = \frac{x^{b}+a^{b}}{x^{b}}$", color="blue")
plt.plot(x_right, f(x_right), color="blue")

# График  2
a = 1
b = 2
def f(x):
    return (x**b+a**b)/x**b

#plt.figure(figsize=(8, 6))генерация нового окна и его параметры
plt.plot(x_left, f(x_left), label=r"$f(x) =  \frac{x^{b}+a^{b}}{x^{b}}$", color="green")
plt.plot(x_right, f(x_right), color="green")

# График  3
a = 2
b = 1
def f(x):
    return (x**b+a**b)/x**b

#plt.figure(figsize=(8, 6))генерация нового окна и его параметры
plt.plot(x_left, f(x_left), label=r"$f(x) =  \frac{x^{b}+a^{b}}{x^{b}}$", color="orange")
plt.plot(x_right, f(x_right), color="orange")
# настройки
plt.ylim(-20,20)
plt.grid()
plt.ylabel("f(x)")
plt.title("График функции с точкой разрыва второго рода")
plt.axvline(d, color='red', linestyle='--')
plt.axhline(w, color='red', linestyle='--', label='асимптоты')
plt.legend()
plt.show()


