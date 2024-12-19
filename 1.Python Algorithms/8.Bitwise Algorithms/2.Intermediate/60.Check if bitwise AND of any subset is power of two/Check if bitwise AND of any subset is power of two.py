# Python3 Program to check if Bitwise AND of any
# subset is power of two

NUM_BITS = 32

# Check for power of 2 or not
def isPowerOf2(num):
	return (num and (num & (num - 1)) == 0)

# Check if there exist a subset whose bitwise AND
# is power of 2.
def checkSubsequence(arr, n):

	# if there is only one element in the set.
	if (n == 1):
		return isPowerOf2(arr[0])

	# Finding a number with all bit sets.
	total = 0
	for i in range(0, NUM_BITS):
		total = total | (1 << i)

	# check all the positions at which the bit is set.
	for i in range(0, NUM_BITS):

		ans = total
		for j in range(0, n):

			# include all those elements whose
			# i-th bit is set
			if (arr[j] & (1 << i)):
				ans = ans & arr[j]

		# check for the set contains elements
		# make a power of 2 or not
		if (isPowerOf2(ans)):
			return True
	return False

# Driver Program
arr = [ 12, 13, 7 ]
n = len(arr)
if (checkSubsequence(arr, n)):
	print ("YES\n")
else:
	print ("NO\n")

# This code is contributed by Manish Shaw
# (manishshaw1)
