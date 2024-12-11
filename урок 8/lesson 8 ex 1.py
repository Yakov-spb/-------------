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


