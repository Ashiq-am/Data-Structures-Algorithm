# Python3 program to calculate the number
# of ordered pairs such that their
# bitwise and is zero

# Naive function to count the number
# of ordered pairs such that their
# bitwise and is 0
def countPairs(a, n):
	count = 0

	# check for all possible pairs
	for i in range(0, n):
		for j in range(i + 1, n):
			if (a[i] & a[j]) == 0:

				# add 2 as (i, j) and (j, i) are
				# considered different
				count += 2
	return count

# Driver Code
a = [ 3, 4, 2 ]
n = len(a)
print (countPairs(a, n))
