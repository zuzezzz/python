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
print(spis1)	

plt.pie(spis1.values(), labels = spis1.keys())
plt.title('Species pie')
plt.show()
plt.savefig('species_pie.png')



'''for i in range(len(f1)):
	data[i] = map(float, data[i].split())
first = [float(line.split()[0]) for line in data]
second = [float(line.split()[1]) for line in data]'''

