#задание 1

import pandas as pd
import numpy as np

a = pd.Series([4.313, 4.338, 4.358, 4.378, 4.4, 4.425, 4.447, 4.468])
print(a)
b = pd.Series(np.arange(0, 20, 2))
print(b)
c = pd.Series({'в': 1, 'траве': 3, 'сидел': 5, 'кузнечик': 7})
print(c)

#2
import pandas as pd
#Получить не пересекающиеся элементы в двух объектах Series или двух столбцах одного Dataframe;
file1 = pd.Series(['bear', 'bird', 'tiger', 'elefant', 
                 'cat', 'dog']) 
  
file2 = pd.Series(['smoke', 'fire', 'cat', 
                 'dog', 'snow', 'pin'])
res = file1[~file1.isin(file2)] 
print(res) 
#3
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
#4
import pandas as pd
df1 = pd.DataFrame ({'country': ['Kazakhstan','Russia'], 'population': [17.024, 1434.5]})
df2 = pd.DataFrame({'counry': ['Japan', 'Norway'], 'population': [180, 560]})
#исходные данные
print (df1)
print (df2)

vertical = pd.concat([df1, df2], axis=0) 
horizont = pd.concat([df1,df2],axis = 1)
print('объединенные данные')
print(vertical)
print(horizont)
#5
#построить график зависимости одного столбца от другого для Dataframe
import matplotlib.pyplot as plt
import pandas as pd
df = pd.DataFrame ({'f':[11,12,16,18,20,21,23,26,27],'U': [0.8,1.1,1.5,0.6,1.8,1.9,2,2.3,2.5]})
print (df)
df.plot(x='f', y='U')
plt.show()                   
 