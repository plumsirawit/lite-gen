import random
a, b = map(int, input().split())

if a == 18:
	x = random.randint(4.5*10**a//1, 5*10**a)
else:
	x = random.randint(1, 10**a)
if b == 18:
	y = random.randint(4.5*10**b//1, 5*10**b)
else:
	y = random.randint(1, 10**b)
print(x)
print(y)