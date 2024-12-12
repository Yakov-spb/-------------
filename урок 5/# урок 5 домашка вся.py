# урок 5 домашка вся
#1 
def acos(x, y) :
    return x  / ((x * x + y * y) ** 0.5)
x1, x2 = map(float,input().split())
y1, y2 = map(float,input().split())
z1, z2 = map(float,input().split())
с = [x1, x2]
acosx = acos(x1, x2)
acosy = acos(y1, y2)
if acosy > acosx :
    acosx = acosy
    с = [y1, y2]
acosz = acos(z1, z2)
if acosz > acosx :
    acosz = acosz
    res = [z1, z2]
print(*с)
#2
def palindrom(n):
    newn = bin(n)[2:]
    if newn == newn[::-1]:
        return newn
    else:
        return ''


n = int(input())
rez = {}
for i in range(n + 1):
    if palindrom(i) != '':
        rez.update({i: palindrom(i)})
print(f'найдено чисел палиндромов {len(rez)}, сами числа {rez}')