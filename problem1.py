l = []
for x in range(1, 1000):
	if (x % 3 == 0) | (x % 5 == 0):
		l.append(x)

print(sum(l))