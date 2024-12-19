# Python3 program to find maximum number of
# 0's in binary representation of a number

# Returns maximum 0's between two immediate
# 1's in binary representation of number
def maxZeros(n):
	# If there are no 1's or there is
	# only 1, then return -1
	if (n == 0 or (n & (n - 1)) == 0):
		return -1

	# loop to find position of right most 1
	# here sizeof is 4 that means total 32 bits
	setBit = 1
	prev = 0
	i = 1
	while(i < 33):
		prev += 1

		# we have found right most 1
		if ((n & setBit) == setBit):
			setBit = setBit << 1
			break

		# left shift setBit by 1 to check next bit
		setBit = setBit << 1

	# now loop through for remaining bits and find
	# position of immediate 1 after prev
	max0 = -10**9
	cur = prev
	for j in range(i + 1, 33):
		cur += 1

		# if current bit is set, then compare
		# difference of cur - prev -1 with
		# previous maximum number of zeros
		if ((n & setBit) == setBit):
			if (max0 < (cur - prev - 1)):
				max0 = cur - prev - 1

			# update prev
			prev = cur
		setBit = setBit << 1

	return max0

# Driver Code
n = 549

# Initially check that number must not
# be 0 and power of 2
print(maxZeros(n))

# This code is contributed by Mohit Kumar
