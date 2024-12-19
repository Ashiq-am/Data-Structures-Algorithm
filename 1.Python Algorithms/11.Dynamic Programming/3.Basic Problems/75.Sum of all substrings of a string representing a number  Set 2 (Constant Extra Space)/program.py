# Python3 program to print sum of all substring of
# a number represented as a string

# Returns sum of all substring of num
def sumOfSubstrings(num):

	sum = 0 # Initialize result

	# Here traversing the array in reverse
	# order.Initializing loop from last
	# element.
	# mf is multiplying factor.
	mf = 1
	for i in range(len(num) - 1, -1, -1):

		# Each time sum is added to its previous
		# sum. Multiplying the three factors as
		# explained above.
		# int(s[i]) is done to convert char to int.
		sum = sum + (int(num[i])) * (i + 1) * mf

		# Making new multiplying factor as
		# explained above.
		mf = mf * 10 + 1

	return sum

# Driver code to test above methods
if __name__=='__main__':
	num = "6759"
	print(sumOfSubstrings(num))
