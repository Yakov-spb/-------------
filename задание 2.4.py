umber = int(input('Введите число: '))
factorial = 1

while number > 1:
    factorial = factorial * number
    number = number - 1

print(factorial)