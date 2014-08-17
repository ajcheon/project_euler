# Find the sum of all the primes below two million.
# 1/4/13

import math 
import time 
  
# FOR DEBUGGING ONLY
def is_prime(n): 
    for i in range (1, n): 
        if n % i == 0 and i != 1 and i != n: 
            return False
    return True
  
#--------------------------------------------- 
  
#limit = 2000000
limit = 300425737571
  
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
  
total = 0
number = 0
for i in range (len(nums)): 
    if nums[i] == True: 
        number = i + 2
        total += number 
  
print "sum of all primes below", limit, ":", total 
t1 = time.time() 
  
print "time elapsed:", t1 - t0