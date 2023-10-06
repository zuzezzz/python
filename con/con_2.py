a, b = map(int, input().split())
if (a % b == 0 or b % a == 0) and a != 1 and b != 1:
	print(0)
else:
	for i in range(max(a, b)):
		if (a + i) % b == 0 and (b + i) % a == 0:
			print(i)
