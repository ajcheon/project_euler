# What is the largest prime factor of the number 600851475143 ? 
# 1/6/13 

import math

def populate(list, n):
	start1 = 0
	cap1 = (int)(n/2)
	start2 = cap1
	cap2 = (int)(n)
	print "cap1:", cap1
	print "start2:", start2

	for i in xrange (start1, cap1):
		n[i] = True
	for j in xrange (start2, cap2):
		n[j] = True

limit = 600851475143
nums = [] # BOOLEAN array!!!!!
nums = populate(nums, limit)
  
pos = 0 # corresponds to n = 2 
while pos < (int)(math.ceil(math.sqrt(limit))): 
    if nums[pos] == False: 
        pos += 1
    else: 
        for i in range (2*pos + 2, len(nums), pos + 2): 
            nums[i] = False
        pos += 1

prime_factors = []
prime_num = 0
for i in range (len(nums)): 
    if nums[i] == True: 
        prime_num = i + 2
        if limit % prime_num == 0:
        	prime_factors.append(prime_num) 

print max(prime_factors)

''' 
total = 0 
number = 0 
for i in range (len(nums)): 
    if nums[i] == True: 
        number = i + 2 
        total += number 
'''