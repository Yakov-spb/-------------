import re
a = 'анннистннвввнн'
k = [_.replace("н", "!") for _ in a]
print(k)
#2
import re
a = 'это задание (домашка) было выполнена'
i = 0
while a[i] != '(':
    i += 1
i += 1
while a[i] != ')':
    print(a[i], end=' ')
    i += 1    

#3
import re
a = 'ананас кегля абстракция'
b= a.split( )
for i in b:
    if i.startswith('а') and i.endswith('я'):
        print(i)