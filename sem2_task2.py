num, word = input().split()
num = int(num)
spis = []
spis2 = []
spis3 = []
spis4 = []
k = len(spis) // num
for i in word:
    spis.append(i)

for i in range(0, len(spis), num):
        spis2 = spis[i:i + num]
        spis2.reverse()
        spis3.append(spis2)

for i in spis3:
    j = ''.join(i)
    spis4.append(j)

string = ''.join(spis4) 
print(string)
