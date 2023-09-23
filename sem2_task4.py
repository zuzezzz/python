list = input().split()
for i in range ( 0, len(list) - 1, 2): list[i], list[i+1] = list[i+1], list[i]
print (list)
