import re
n = (input())
n = n.upper()
m = re.match(r"[ABEMHOPCTYX]{1}\d{3}[ABEMHOPCTYX]{2}\d{2}", n)
k = re.match(r"[ABEMHOPCTYX]{1}\d{3}[ABEMHOPCTYX]{2}\d{3}", n)
if m:
 print (f'{m.group(0)} - это просто автомобиль')
elif k:
 print (f'{k.group(0)} - это такси')
else: 
 print('это не номер')

#2
import re
enter = 'посмотрите, как работают простые шаблоны и квантификаторы'
n = re.fullmatch(r"[\b[a-zа-яё]+\b ]" , enter)
print (n)
count = len(' '.join(n).split())
print (n)
#3
import re
messege = 'Уважаемые! Если вы к 09:00 не вернете чемодан.\n\
То уже в 09:00:01 я за себя не отвечаю!\n\
PS Со времнем 25:50 все нормально.'
s = re.findall(\
'((?:[01]\d|2[0-3])\:(?:[0-5]\d)(?:\:[0-5]\d)?)',messege)
print(s)
new = re.sub(s, "(TBD)", messege)
print (new)