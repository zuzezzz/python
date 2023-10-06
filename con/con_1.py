spis =  list(input().split())
print(spis)
'''for i in range(1, len(spis)):
	if int(spis[-i] + spis[-i - 1]) > int(spis[-i - 1] + spis[-i]):
		spis[-i], spis[-i - 1] = spis[-i - 1], spis[-i]
str = ''.join(spis)
print(str)'''

for j in range(len(spis) - 1):
	for i in range(len(spis) - j - 1):
		if spis[i] + spis[i + 1] <  spis[i + 1] + spis[i]:
			spis[i], spis[i + 1] = spis[i + 1], spis[i]


print(str(''.join(spis)))
