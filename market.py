import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sn

df=pd.read_csv('C:\\Users\\Dell\\Desktop\\stock\\sales.csv')
diff_status=df.status.value_counts()
print(diff_status[2])
total=int(df.shape[0])


order_cancel=(int(diff_status[0])/total)*100
order_completed=(int(diff_status[1])/total)*100
order_received=(int(diff_status[2])/total)*100
order_refunded=(int(diff_status[3])/total)*100
order_refund=(int(diff_status[4])/total)*100
order_cod=(int(diff_status[5])/total)*100
paid=(int(diff_status[6])/total)*100
closed=(int(diff_status[7])/total)*100
payment_review=(int(diff_status[8])/total)*100
pending=(int(diff_status[9])/total)*100
processing=(int(diff_status[10])/total)*100
holded=(int(diff_status[11])/total)*100
pending_paypal=(int(diff_status[12])/total)*100
arr=np.array([order_cancel,order_completed,order_received,order_refunded,order_refund,order_cod,paid,closed,payment_review,pending,processing,holded,pending_paypal])
label=['canceled','complete','received','order_refunded','refund','cod',
                     'paid','closed','payment_review','pending','processing','holded','pending_paypal']
plt.pie(arr,autopct='%1.1f%%',explode=[0.05,0,0.01,0.01,0.01,0.01,0.01,0.01,0.02,0.02,0.02,0.03,0.03])
plt.legend(loc='upper left',labels=label)
plt.show()


