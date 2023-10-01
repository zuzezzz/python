from matplotlib import pyplot as plt
import pandas as pd
from datetime import datetime

data = pd.read_csv('BTC_data.csv')
date = data['time'].tolist()
price = data['close'].tolist()

for i in range(len(date)):
    date[i] = date[i][0:10]
    date[i] = datetime.strptime(date[i], '%Y-%m-%d').strftime('%d-%m-%Y')
    
xtiks = [date[0]]
for i in range(1, 10):
    xtiks.append(date[len(date) // 10 * i])
xtiks.append(date[-1])

ytiks = [0]
for i in range(1, 10):
    ytiks.append(max(price) // 10 * i)
ytiks.append(max(price))

plt.figure(figsize = (16, 9), dpi = 100)
plt.plot(date, price, linewidth = 1)
plt.title('BTC rate from ' + date[0] + ' to ' + date[-1], fontdict={'fontname': 'sans-serif', 'fontsize': 20})
plt.xlabel('Date')
plt.ylabel('Price')
plt.xticks(xtiks)
plt.yticks(ytiks)
plt.grid()

plt.show()

