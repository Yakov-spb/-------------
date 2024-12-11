import re
enter = 'посмотрите, как работают простые шаблоны и квантификаторы'
n = re.fullmatch(r"[\b[a-zа-яё]+\b ]" , enter)
print (n)
count = len(' '.join(n).split())
print (n)