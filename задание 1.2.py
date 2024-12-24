#1.2 сумма четных чисел

a=int(input("a = "))
b=int(input("b = "))
sum_even = 0
for i in range(a, b + 1):
    if i % 2 == 0:#шаг 2
        sum_even += i
print(sum_even)