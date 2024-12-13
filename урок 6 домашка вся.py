#1
import random

n = [[(random.randint(1, 9)), (random.randint(1, 9)),( random.randint(1, 9)) ], [(random.randint(1, 9)), (random.randint(1, 9)), (random.randint(1, 9)) ], [(random.randint(1, 9)), (random.randint(1, 9)), (random.randint(1, 9))]]

print('матрица 1 ')
for i in n:
  print(' '.join(list(map(str, i))))
a= list() #пустой спиок
a.extend(n[1])#выбор номера строки и добавления в список(строка 2)
print(a)
l = max(a)
print (l)
b=list()
for i in n:
  b.append(i[2])#добавление в новый список значений по i(строке)по индексу в рамках одной строке
  print('второй массив данных',b)
g = max(b) 
print ('максимальные значения по 3 му столбцу',g)
#2
n = 3
arr = list()
#Заполняем массив 9-ми
for i in range(n):
  arr.append([9]*n)
#Вывод исходного массива
for i in range(n):
  for j in range(n):
    print(arr[i][j], end = ' ')
  print()