import math
import time


def is_prime(n):
	for i in range (1, n):
		if n % i == 0 and i != 1 and i != n:
			return False
	return True

#---------------------------------------------
outfile = open ("problem_10_times.txt", 'a')
cap = 5000000
step = 1000
for limit in range (10, cap + step, step):
	#limit = 2000000

	nums = [True] * (limit - 1)

	t0 = time.time()
	pos = 0 # corresponds to n = 2
	while pos <  (int)(math.ceil(math.sqrt(limit))):
		if nums[pos] == False:
			pos += 1
		else:
			for i in range (2*pos + 2, len(nums), pos + 2):
				nums[i] = False
			pos += 1
	t1 = time.time()
	outfile.write(str(limit) + "\t" + str(t1 - t0) + "\n")
	print "For", limit, "primes:", t1 - t0, "seconds"

	# total = 0
	# number = 0
	# for i in range (len(nums)):
	# 	if nums[i] == True:
	# 		number = i + 2
	# 		#if not is_prime(number):
	# 			#print number, "is not prime!"
	# 		total += number

	# print "sum of all primes below", limit, ":", total