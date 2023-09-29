import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('iris_data.csv')
sep_len = data['SepalLengthCm'].tolist()
sep_wid = data['SepalWidthCm'].tolist()
pet_len = data['PetalLengthCm'].tolist()
pet_wid = data['PetalWidthCm'].tolist()
spec = data['Species'].tolist()


spis1 = {} 
for i in spec:
	spis1[i] = spec.count(i)	
plt.pie(spis1.values(), labels = spis1.keys())
plt.title('Species pie')
#plt.show()
plt.savefig('species_pie.png') 

spis2 = {}
spis2['less than 1.2'] = len([i for i in pet_len if i < 1.2])
spis2['between 1.2 and 1.5'] = len([i for i in pet_len if i >= 1.2 and i <= 1.5])
spis2['more than 1.5'] = len([i for i in pet_len if i > 1.5])
plt.pie(spis2.values(), labels = spis2.keys())
plt.title('Petal length pie')
#plt.show()
plt.savefig('pet_len_pie.png') 




