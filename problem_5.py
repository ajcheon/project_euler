# smallest positive number that is evenly divisible by all numbers from 1 to 20 
  
keep_going = True
incr = 10
  
while keep_going: 
    tally = 0
    for i in range (1, 21): 
        if incr % i == 0: 
            tally += 1 
    if tally == 20: 
        print inc
        keep_going = False
    incr += 1
