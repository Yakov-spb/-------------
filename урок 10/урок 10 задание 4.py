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