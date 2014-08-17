# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

# 1/1/14

import math
import time

a, b, c, = 1, 1, 1

t1 = time.time()
keep_going = True
while keep_going and a <= 1000:
	b = 1
	while keep_going and b <= 1000:
		c = math.sqrt(a**2 + b**2)
		#print c
		if  c  - round(c) == 0.0: # legitimate pythagorean triple
			#print "a:", a, "b:", b, "c:", c, "is a pyth triple"
			if a + b + c == 1000: # fits given rule
				print "a * b * c =", (int)(a * b * c)
				print "a:", a, "b:", b, "c:", (int)(c)
				print "a + b + c =", a + b + c
				keep_going = False
		b += 1
	a += 1
t2 = time.time()

print "Time elapsed:", t2 - t1