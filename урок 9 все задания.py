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

#2
import numpy as np
#!!!!!!!!!!!!!!!!!!
from matplotlib import pyplot as plt
from matplotlib import cbook
from matplotlib.ticker import *
from mpl_toolkits.axes_grid1.inset_locator import inset_axes
# проверить что все библиотеки нужны для корректной работы программы

fig, ax = plt.subplots(figsize=(8, 6))

x1, x2, y1, y2 = 247, 248, 0.99, 1.01  
axins = ax.inset_axes(
    [0.5, 0.5, 0.47, 0.47],
    xlim=(x1, x2), ylim=(y1, y2), xticklabels=[], yticklabels=[])


def f(x, a, b):
    if x != 0:
        return (pow(x,b) + pow(a,b)) / pow(x,b)
    else:
        return '!'

def raz(a, b):
    for i in range(-30, 30):
        if f(i, a, b) == '!':
            return i

for i in ax, axins:
    xright1 = np.linspace(raz(1, 1) + 1, raz(1, 1) + 250)
    yright1 = [f(i, 1, 1) for i in xright1]
    i.plot(xright1, yright1, label=r'$f(x)=\frac{x^{1} + 1^{1}}{x^{1}}$', color='red')

    xright2 = np.linspace(raz(2, 1) + 1, raz(2, 1) + 250)
    yright2 = [f(i, 2, 1) for i in xright2]
    i.plot(xright2, yright2, label=r'$f(x)=\frac{x^{1} + 2^{1}}{x^{1}}$', color='blue')

    xright3 = np.linspace(raz(1, 2) + 1, raz(1, 2) + 250)
    yright3 = [f(i, 1, 2) for i in xright3]
    i.plot(xright3, yright3, label=r'$f(x)=\frac{x^{2} + 1^{2}}{x^{2}}$', color='green')

    i.grid(which='major', linewidth=1)
    i.grid(which='minor', color='grey' ,linewidth=0.5)
    i.xaxis.set_minor_locator(AutoMinorLocator())
    i.yaxis.set_minor_locator(AutoMinorLocator())
    i.tick_params(which='major', length=10, width=2)
    i.tick_params(which='minor', length=5, width=1)

plt.xlabel('x')  # для оси x
plt.ylabel('y')  # для оси y
plt.title('график')  # заголовок
plt.legend()

plt.ylim(0.5, 2)
plt.xlim(0, 250)

ax.indicate_inset_zoom(axins, edgecolor="red")

plt.show()

#3
fig, ax = plt.subplots(figsize=(8, 6))

x1, x2, y1, y2 = -247, -248, 0.99, 1.01
axins = ax.inset_axes(
    [0.5, 0.5, 0.47, 0.47],
    xlim=(x1, x2), ylim=(y1, y2), xticklabels=[], yticklabels=[])

import numpy as np
from matplotlib import pyplot as plt
#точка разрыва
d = 0
w=1
x_left = np.linspace(-2, d - 0.08, 2000)  # Левее точки разрыва
x_right = np.linspace( d + 0.08, 2, 2000)


#график 1
a = 1
b = 0.5
def f(x):
    return (x**b+a**b)/x**b

#plt.figure(figsize=(8, 6))

plt.plot(x_right, f(x_right), color="blue")

# График  2
a = 1
b = -0.5
def f(x):
    return (x**b+a**b)/x**b

#plt.figure(figsize=(8, 6))генерация нового окна и его параметры

plt.plot(x_right, f(x_right), color="green")

# График  3
a = 1
b = -1.5
def f(x):
    return (x**b+a**b)/x**b

#plt.figure(figsize=(8, 6))генерация нового окна и его параметры
plt.plot(x_left, f(x_left), label=r"$f(x) =  \frac{x^{b}+a^{b}}{x^{b}}$", color="orange")
plt.plot(x_right, f(x_right), color="orange")
# настройки

plt.xlim(0.25,2)
plt.ylim(-20,20)
plt.grid()
plt.ylabel("f(x)")
plt.title("График номер 3")
plt.axhline(d, color='red', linestyle='--')
plt.legend()
plt.show()
#4
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


