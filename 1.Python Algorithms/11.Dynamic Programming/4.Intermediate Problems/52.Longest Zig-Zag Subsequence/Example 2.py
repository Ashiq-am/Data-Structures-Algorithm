# Python3 program to find the maximum
# length of zig-zag sub-sequence in
# given sequence

# Function to calculate maximum length
# of zig-zag sub-sequence in given sequence.


def maxZigZag(seq, n):

	if (n == 0):
		return 0

	lastSign = 0

	# Length is initialized to 1 as that is
	# minimum value for arbitrary sequence
	length = 1

	for i in range(1, n):
		Sign = signum(seq[i] - seq[i - 1])

		# It qualifies
		if (Sign != lastSign and Sign != 0):

			# Updating lastSign
			lastSign = Sign
			length += 1

	return length

# Signum function :
# Returns 1 when passed a positive integer
# Returns -1 when passed a negative integer
# Returns 0 when passed 0.


def signum(n):

	if (n != 0):
		return 1 if n > 0 else -1
	else:
		return 0


# Driver code
if __name__ == '__main__':

	sequence1 = [1, 3, 6, 2]
	sequence2 = [5, 0, 3, 1, 0]

	n1 = len(sequence1)
	n2 = len(sequence2)

	# Function call
	maxLength1 = maxZigZag(sequence1, n1)
	maxLength2 = maxZigZag(sequence2, n2)

	print("The maximum length of zig-zag sub-sequence "
		"in first sequence is:", maxLength1)
	print("The maximum length of zig-zag sub-sequence "
		"in second sequence is:", maxLength2)
