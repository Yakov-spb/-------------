a, b = input().split()
a, b = map(int, (a, b))
if b !=0:
    c = a/b
    print('результат деления',c)
else:
        print("делить на ноль нельзя!")
        a = input("введите стоимость покупки \n")
    
a=float(a) 
if  a > 20:
    d = a * 0,35
    
    b = a - d
   
    print ("размер скидки", d,"стоимость со скидкой", b)
else:
    print("скидка не зачтена,итог:",a)
    a = input()
if not a.isdigit():
    a=int(a) 
else:
    a=int(a) 
    a > 0 and a < 13
if a==1 or a==2  or a==12:
    print("время года -зима")
else:
    if a==3 or a==4 or a==5:
        print("время года весна")
    else:
        if a==6 or a==7 or a ==8:
            print("время года лето")
        else:
            if a==9 or a==10 or a==11:
                print("время года - осень")
            else:
                print("введите число от 1 до 12 ")