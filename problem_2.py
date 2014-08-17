# sum of all fibonacci evens up to 4,000,000 (1, 2, 3, 5, ... , +- 4,000,000)

fib_list = [1, 2]

num = 0
i = 1
while True:
	num =  fib_list[i] + fib_list[i-1]
	if num <= 4000000:
		fib_list.append(num)
		i += 1
	else:
		break
#print fib_list

sum = 0
for i in range (len(fib_list)):
	if fib_list[i] % 2 == 0:
		#print fib_list[i]
		sum += fib_list[i]
print sum