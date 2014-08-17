# largest palindrome made from the product of two 3-digit numbers

palins = []

for i in range (100, 1000):
	for j in range (100, 1000):
		prod = str(i * j)
		if prod == prod[::-1]:
			palins.append((int)(prod))

print max(palins)