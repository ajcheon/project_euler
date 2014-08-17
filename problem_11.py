import time
total = 0
times = []
outfile = open("problem_11_times.txt", 'a')
for repeat in range (0, 100):	
	t0 = time.time()
	#--------------------put grid stuff into 2D list "nums"---------------------

	gridfile = open ("problem_11_grid.txt", 'r')
	col = 0
	nums = [[0 for x in range(20)] for y in range(20)] 
	for line in gridfile:
		#print line
		row_pos = 0
		for i in range (0, len(line) - 2, 3):

			if line[i] == "0":
				num = (int)(line[i + 1].strip())
			else:
				num = (int)(line[i : i + 2].strip())

			if row_pos == 19: # reached row size limit
				nums[col][row_pos] = num
				row_pos += 1 # increases after step through each number in a row
				col += 1
			else: # haven't yet reached row size limit
				nums[col][row_pos] = num
				row_pos += 1 # increases after step through each number in a row

	# for each_row in nums:
	# 	print each_row

	#----------------------------------------------------------------------------

	products = []

	# LEFT/RIGHT
	for row in range (0, 20):
		for col in range (0, 17):
			prod = 1
			for i in range (col, col + 4):
				prod *= nums[row][i]
				#print nums[row][i]
			products.append(prod)

	# DOWN/UP
	for row in range (0, 17):
		for col in range (0, 20):
			prod = 1
			for i in range (row, row + 4):
				prod *= nums[i][col]
			products.append(prod)
			
	# DIAGONAL (\)
	for row in range (0, 17):
		for col in range (0, 17):
			prod = 1
			rows = row
			for i in range (col, col + 4):
				prod *= nums[rows][i]
				#print nums[rows][i]
				rows += 1
			products.append(prod)

	# DIAGONAL (/)
	for row in range (3, 20):
		for col in range (0, 17):
			prod = 1
			cols = col
			for i in range (row, row - 4, -1):
				prod *= nums[i][cols]
				#print nums[i][cols]
				cols += 1
			products.append(prod)

	gridfile.close()

	t1 = time.time()

	times.append(t1 - t0)
	outfile.write(str(t1 - t0) + "\n")

outfile.close()
print "max time:", max(times)
print "min time:", min(times)