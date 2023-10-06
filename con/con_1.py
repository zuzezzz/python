spis =  list(input().split())

for j in range(len(spis) - 1):
	for i in range(len(spis) - j - 1):
		if spis[i] + spis[i + 1] <  spis[i + 1] + spis[i]:
			spis[i], spis[i + 1] = spis[i + 1], spis[i]

print(str(''.join(spis)))
