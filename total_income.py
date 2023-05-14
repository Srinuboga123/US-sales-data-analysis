import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sn


df=pd.read_csv('C:\\Users\\Dell\\Desktop\\sales.csv')
l=[df.loc[df['year']==2020]['total'].sum(), df.loc[df['year']==2021]['total'].sum()]
y=[2020,2021]
dict={'year':y,'income':l}
data1=pd.DataFrame(dict,index=[0,1])

sn.lineplot(x='year',y='income', data=data1)
#plt.bar(x=y, y=l, height=5)
#sn.legend(loc='upper left', labels=['2020 income','2021 income'])

plt.show()
