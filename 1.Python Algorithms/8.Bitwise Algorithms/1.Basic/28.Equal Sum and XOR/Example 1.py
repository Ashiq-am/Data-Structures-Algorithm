# Python3 program to print count
# of values such that n+i = n^i

# function to count number
# of values less than
# equal to n that satisfy
# the given condition
def countValues (n):
	countV = 0;

	# Traverse all numbers
	# from 0 to n and
	# increment result only
	# when given condition
	# is satisfied.
	for i in range(n + 1):
		if ((n + i) == (n ^ i)):
			countV += 1;

	return countV;

# Driver Code
n = 12;
print(countValues(n));

# This code is contributed by mits
