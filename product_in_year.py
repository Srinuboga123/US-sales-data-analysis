import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sn


df=pd.read_csv('C:\\Users\\Dell\\Desktop\\sales.csv')
dict={'items':df[df['Place Name']=='Vinson']}

a=sn.barplot(y='year',x='category', hue='year', data=df)
a.set(ylabel='count of goods', )
plt.show()