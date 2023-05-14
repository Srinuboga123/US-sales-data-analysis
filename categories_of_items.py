import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sn

df=pd.read_csv('C:\\Users\\Dell\\Desktop\\sales.csv')
sn.countplot(y='category', data=df)
plt.show()