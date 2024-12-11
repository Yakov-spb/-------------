#построить график зависимости одного столбца от другого для Dataframe
import matplotlib.pyplot as plt
import pandas as pd
df = pd.DataFrame ({'f':[11,12,16,18,20,21,23,26,27],'U': [0.8,1.1,1.5,0.6,1.8,1.9,2,2.3,2.5]})
print (df)
df.plot(x='f', y='U')
plt.show()                   


