x  = list(map(int, input().split()))
y = list(map(int, input().split()))
totalx = []
totaly = []
for i in range(len(x)):
    for j in range(len(y)):
        totalx.append(x[i] * y[j])
        totaly.append(x[i] ** 2)
mnk = ((sum(totalx) / len(x)) / (sum(totaly) / len(y)))
print(mnk)
