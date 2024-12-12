import matplotlib.pyplot as plt
import pandas as pd
spisok = pd.Series({0: 'female',1: 'male',2: 'male',3: 'female',4: 'female',5: 'male',
  6: 'male',7: 'male',8: 'male',9: 'female',10: 'female',11: 'female',12: 'female',
  13: 'female',14: 'male',15: 'male',16: 'male',17: 'male',18: 'male',19: 'female',
  20: 'female',21: 'female',22: 'male',23: 'male',24: 'male',25: 'male',26: 'female',
  27: 'female',28: 'male',29: 'female',30: 'male',31: 'female',32: 'female',
  33: 'male',34: 'female'})

x = spisok.value_counts().index
y = spisok.value_counts().values
plt.bar(x, y, color=['pink', 'blue'])
plt.xlabel('количество учеников')  # для оси x
plt.ylabel('пол учеников')  # для оси y
plt.title('соотношение студентов')
plt.show()