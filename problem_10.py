# Find the sum of all the primes below two million.

import math
import time

primes = []
limit = 10000
# for candidate in range (2, limit):
# 	#for i in range (1, (int)(math.sqrt(limit))):
# 	for i in range (1, limit):

# 		if candidate % i == 0 and i != 1 and i != candidate: # NOT prime
# 			break
# 		else:
# 			#if i == (int)(math.sqrt(candidate)):
# 			if i == candidate:	
# 				primes.append(candidate)
# 				print candidate, "is prime"
# print "Sum of primes:", sum(primes)

outfile = open("problem_10_times.txt", 'a')
for limit in range (0, 1000, 10):
	t0 = time.time()
	for candidate in range (2, limit):
		#for i in range (1, (int)(math.ceil((math.sqrt(limit))))):
		for i in range (1, limit):

			if candidate % i == 0 and i != 1 and i != candidate: # NOT prime
				break
			else:
				#if i == (int)(math.ceil(math.sqrt(candidate))):
				if i == candidate:	
					primes.append(candidate)
					#print candidate, "is prime"
	#print "Sum of primes:", sum(primes)
	t1 = time.time()

	#print "Limit:", limit, "\t\t\tsum of primes:", sum(primes)
	print "To find all primes below", limit, ":", t1 - t0, "sec"
	outfile.write(str(limit) + "\t" + str(t1 - t0) + "\n")
