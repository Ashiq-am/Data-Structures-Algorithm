# Python3 Program to count
# reflexive relations
# on a set of first n
# natural numbers.


def countReflexive(n):

	# Return 2^(n*n - n)
	return (1 << (n*n - n));

# driver function
n = 3
ans = countReflexive(n);
print (ans)

# This code is contributed by saloni1297
