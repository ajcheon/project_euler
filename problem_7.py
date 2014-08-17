# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?

# 12/31/13

import math 
import time

# candidate = 2
# primes_so_far = 0
# while True:
# 	count = 0
# 	for i in range (1, candidate + 1):
# 		if candidate % i == 0 and i != 1 and i != candidate: # NOT prime
# 			break
# 		else:
# 			count += 1
# 		if count == candidate:
# 			primes_so_far += 1
# 	if primes_so_far == 2500:
# 		print candidate
# 		break
# 	candidate += 1

outfile = open ("prime_times.txt", 'a')
for limit in range (1, 1500):

	candidate = 3
	primes_so_far = 1
	keep_going = True
	# limit = 10001

	keep_going = True
	t0 = time.time()

	i = 1
	while i <= candidate and keep_going:
		if candidate % i == 0 and i != 1 and i != candidate: # NOT prime
			i = 1 # reset
			candidate += 2 # move on with the next candidate
		else: # possibly prime
			i += 1
		if i == candidate:
			primes_so_far += 1
			#print "primes so far: ", primes_so_far
			i = 1 
			candidate += 2
		if primes_so_far == limit:
			keep_going = False
			print "Prime number # ", primes_so_far, " is ", candidate - 2

	t1 = time.time()
	total_time = t1 - t0
	print "For", limit, " primes, ", "time elapsed: ", total_time, " sec\n\n"

	outfile.write(str(limit) + "\t\t\t" + str(total_time) + "\n")

outfile.close()
