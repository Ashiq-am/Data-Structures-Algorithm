# A simple recursive Python3 program to
# find maximum sum by recursively breaking
# a number in 3 parts.

# Function to find the maximum sum
def breakSum(n) :

	# base conditions
	if (n == 0 or n == 1) :
		return n

	# recursively break the number and
	# return what maximum you can get
	return max((breakSum(n // 2) +
				breakSum(n // 3) +
				breakSum(n // 4)), n)

# Driver Code
if __name__ == "__main__" :

	n = 12
	print(breakSum(n))

