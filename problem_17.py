# If the numbers 1 to 5 are written out in words: 
# one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

# If all the numbers from 1 to 1000 (one thousand) inclusive were written 
# out in words, how many letters would be used?


# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) 
# contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.

# METHOD: 1) Populate hash of 1-1000 of int : word. 2) Loop through entire hash and gather strings for tootal length.

limit = 1000
num2word = {1:'one', 2: 'two', 3: 'three', 4:'four', 5:'five', 
			6:'six', 7:'seven', 8:'eight', 9:'nine', 10:'ten',
			11:'eleven', 12:'twelve', 13:'thirteen', 14:'fourteen',
			15:'fifteen', 16:'sixteen', 17:'seventeen', 18:'eighteen',
			19:'nineteen', 20:'twenty'}

def tens_ones(tens_place, ones_place):
	if tens_place < 2 or tens_place > 9 or ones_place > 9:
		print "ERROR: Invalid function call in tens_ones()."

	str1 = ''
	if ones_place !=0:
		str2 = num2word[ones_place]
	else:
		str2 = ''

	if tens_place == 2:
		str1 = 'twenty'
	elif tens_place == 3:
		str1 = 'thirty'
	elif tens_place == 4:
		str1 = 'forty'
	elif tens_place == 5:
		str1 = 'fifty'
	elif tens_place == 6:
		str1 = 'sixty'
	elif tens_place == 7:
		str1 = 'seventy'
	elif tens_place == 8:
		str1 = 'eighty'
	elif tens_place == 9:
		str1 = 'ninety'

	return str1 + str2  # e.g. 98 --> 'ninetyeight'

def hundreds(hund_place, trail): # e.g. 512 --> hund_place = 5, trail = 12
	str1 = num2word[hund_place] # e.g. hund_place = 4 --> str1 = 'four'
	if trail == '00': # e.g. 100, 300, 900
		str2 = 'hundred'
	elif trail[0] == '0' and trail[1] != '0':
		str2 = 'hundredand' + num2word[(int)(trail[1])] # e.g. 309 --> trail[0] = 0, trail[1] = 9 --> str2 = 'hundrednine'
	else:
		str2 = 'hundredand' + num2word[(int)(trail)]	

	return str1 + str2

def pop_twodigit(n):
	tens = (int)(str(n)[0]) # tens = first digit in 2-digit number from 21-99
	ones = (int)(str(n)[1])
	num2word[n] = tens_ones(tens, ones)

def pop_threedigit(n):
	hundr = (int)(str(n)[0])
	remain = str(n)[1:]
	num2word[n] = hundreds(hundr, remain)


for i in range (21, limit + 1):
	if i >= 21 and i <= 99:
		pop_twodigit(i)
	if i >= 100 and i <= 999:
		pop_threedigit(i)
	if i == 1000:
		num2word[1000] = 'onethousand'

# for key in num2word:
#  	print key, ":", num2word[key]

total_len = 0
for i in range (1, limit + 1):
	total_len += len(num2word[i])
	# print i, "--", num2word[i], "|", len(num2word[i])
	# if str(i)[1:] == '00':
	# 	print "\n\n"
print total_len
