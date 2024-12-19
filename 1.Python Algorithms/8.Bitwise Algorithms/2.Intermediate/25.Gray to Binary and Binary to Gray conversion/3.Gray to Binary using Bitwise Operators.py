# Python3 code for above approach
def binaryConverter(n):
	res = n

	while n > 0:
		n >>= 1
		res ^= n

	return res


n = 4
print(binaryConverter(n))

# This code is contributed by sshrey47
