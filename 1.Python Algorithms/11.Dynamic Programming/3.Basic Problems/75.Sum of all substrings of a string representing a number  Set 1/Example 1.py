# Python program to print
# sum of all substring of
# a number represented as
# a string

# Returns sum of all
# substring of num
def sumOfSubstrings(num):
	n = len(num)

	# allocate memory equal
	# to length of string
	sumofdigit = []

	# initialize first value
	# with first digit
	sumofdigit.append(int(num[0]))
	res = sumofdigit[0]

	# loop over all
	# digits of string
	for i in range(1, n):
		numi = int(num[i])

		# update each sumofdigit
		# from previous value
		sumofdigit.append((i + 1) *
						numi + 10 * sumofdigit[i - 1])

		# add current value
		# to the result
		res += sumofdigit[i]

	return res

# Driver code
num = "1234"
print(sumOfSubstrings(num))

