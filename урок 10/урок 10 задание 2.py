import pandas as pd
#Получить не пересекающиеся элементы в двух объектах Series или двух столбцах одного Dataframe;
file1 = pd.Series(['bear', 'bird', 'tiger', 'elefant', 
                 'cat', 'dog']) 
  
file2 = pd.Series(['smoke', 'fire', 'cat', 
                 'dog', 'snow', 'pin'])
res = file1[~file1.isin(file2)] 
print(res)  