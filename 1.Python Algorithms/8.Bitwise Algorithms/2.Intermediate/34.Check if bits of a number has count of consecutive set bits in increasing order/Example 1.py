# Python3 program to find if bit-pattern
# of a number has increasing value of
# continuous-1 or not.

# Returns true if n has increasing count of
# continuous-1 else false


def findContinuous1(n):

	# store the bit-pattern of n into
	# bit bitset- bp
	bp = list(bin(n))

	bits = len(bp)

	# set prev_count = 0 and curr_count = 0.
	prev_count = 0
	curr_count = 0

	i = 0
	while (i < bits):
		if (bp[i] == '1'):

			# increment current count of continuous-1
			curr_count += 1
			i += 1

		# traverse all continuous-0
		elif (bp[i - 1] == '0'):
			i += 1
			curr_count = 0
			continue

		# check prev_count and curr_count
		# on encounter of first zero after
		# continuous-1s
		else:
			if (curr_count < prev_count):
				return 0
			i += 1
			prev_count = curr_count
			curr_count = 0

	# check for last sequence of continuous-1
	if (prev_count > curr_count and (curr_count != 0)):
		return 0

	return 1


# Driver code
n = 179
if (findContinuous1(n)):
	print("Yes")
else:
	print("No")

# This code is contributed by SHUBHAMSINGH10
