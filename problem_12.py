def get_Tri_num(n):
	sum = 0
	for i in range (1, n + 1):
		sum += i
	return sum

def get_factors(n):
	factors = []
	for i in range (1, n + 1):
		if n % i == 0:
			factors.append(i)
	return factors

i = 10000
keep_going = True
while keep_going:
	tri_num = get_Tri_num(i)
	print "factors so far:", len(get_factors(tri_num))
	if len(get_factors(tri_num)) > 1:
		print tri_num
		keep_going = False
	else:  
		i -= 1