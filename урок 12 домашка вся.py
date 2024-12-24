import pandas as pd

#задание 2
df = pd.read_csv('random\Mall_Customers.csv')
w = df[df['Genre'] == 'Female']
w_income = sum(w['Annual Income (k$)'])/len(w)
print(w_income)


#задание 3
df = pd.read_csv('random\Mall_Customers.csv')

w = df[df['Genre'] == 'Female']
w_max = w['CustomerID'].where(w['Annual Income (k$)'] == max(w['Annual Income (k$)'])).dropna()
print(w_max.index)

m = df[df['Genre'] == 'Male']
m_max = m['CustomerID'].where(m['Annual Income (k$)'] == max(m['Annual Income (k$)'])).dropna()
print(m_max.index)
# задание 4 график


import matplotlib.pyplot as plt

df = pd.read_csv('random\Mall_Customers.csv')

m = df[df['Genre'] == 'Male']
data = m.groupby('Age')['Annual Income (k$)'].mean()
plt.plot(data)
#построение графика
plt.show()
#задние  5 граaики
import matplotlib.pyplot as plt
fig, ax = plt.subplots(figsize=(10, 6))
df = pd.read_csv('random\Mall_Customers.csv')

m = df[df['Genre'] == 'Male']
w = df[df['Genre'] == 'Female']
data_m = m.groupby('Annual Income (k$)')['Spending Score (1-100)'].mean()
data_w = w.groupby('Annual Income (k$)')['Spending Score (1-100)'].mean()3
#постороение
data_m.plot.bar(color='red')
data_w.plot.bar(color='green')
plt.show()