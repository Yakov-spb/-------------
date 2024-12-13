# задание 1
import math

r = int(input())
print(round(2 * math.pi * r, 2))
print(round(math.pi * math.pow(r, 2), 2))

# задание2 
x = 10
y = 55
print(x, y)#меняем переменные местами
x, y = y, x
print(x, y)

# задание 3 
L = int(input())
g = 9.81
print((2 * math.pi * math.sqrt(float(L) / g), 2))