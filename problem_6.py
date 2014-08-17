# difference between the sum of the squares of the first one hundred natural numbers
# and the square of the sum

# 12/31/13

sum_of_squares = 0
for i in range (1, 101):
	sum_of_squares += i ** 2

square_of_sum = 0
total = 0
for j in range (1, 101):
	total += j
square_of_sum = total ** 2

print square_of_sum - sum_of_squares
