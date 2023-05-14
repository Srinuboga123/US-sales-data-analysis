import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sn


df=pd.read_csv('C:\\Users\\Dell\\Desktop\\sales.csv')



e=sn.barplot(x='age',y='total', data=df, color='b')
e.set(ylabel='total_revenu=graph_value*e+06')
#sn.heatmap(df.corr(), cbar=True, linewidths=0.1)
plt.show()

