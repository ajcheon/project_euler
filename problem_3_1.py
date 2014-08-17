import math


def is_prime(n):
	count = n 
	while count >= 1:
		if n % count == 0 and count != 1 and count != n:
			return False
		count -= 1
	return True



limit = 600851475143
#i = limit
i = (int)(math.sqrt(limit))

#while i >= (int)(math.sqrt(limit)):
while i >= 1:
	#print "Trying:", i
	if limit % i == 0:
		print "divisible by", i, "\n\n"
		
		
		if is_prime(i):
			print "Largest prime factor of", limit, ":", i
			break
		else:
			print i, "is not prime"
		
	# else:
	# 	print "not divisible by", i
	i -= 1
