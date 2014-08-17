# Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.

num_length = 50
nums = []
totals = [] # array whose elements are the digits of the huge total (each elem = each digit)

# read in text file
#f = open ("problem_13_numbers.txt", 'r')
f = open ("problem_13_numbers.txt", 'r')
for line in f:
	num = str(line.strip())[::-1] # invert digits to make calculation easier
	nums.append(num)
print nums
f.close()

col = 0
while col < num_length:
	col_total = 0

	for i in range (len(nums)):
		col_total += (int)(nums[i][col]) # takes an element of nums (a number), grabs a digit from current column
	print "Column", col, "col total:", col_total
	#print col_total
	col_total_len = len(str(col_total))
	col_total = str(col_total) # make col_total into a string
	#print "size of array:", len(totals)

	if col == 0:
		totals.append((int)(col_total[-1]))  # append the ones digit ONLY

	else:
		if col >= len(totals):
			totals.append((int)(col_total[-1]))
		else:
			totals[col] = totals[col] + (int)(col_total[-1]) # add carry-over digit with column total for that particular col
	
	if (int)(col_total) >= 10 or totals[col] + (int)(col_total) >= 10:
		col_total = col_total[::-1] # invert digits in col_total
		for j in range (1, col_total_len):  # append the rest of the digits
			totals.append((int)(col_total[j])) 

	col += 1

print len(totals)

print totals[::-1]