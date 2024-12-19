# Python3 program to check
# if given number is
# power of 4 or not
import math


def isPowerOfFour(n):
	return (n > 0 and 4**int(math.log(n, 4)) == n)


# Driver code
if __name__ == '__main__':

	test_no = 64

	if (isPowerOfFour(test_no)):
		print(test_no, " is a power of 4")
	else:
		print(test_no, " is not a power of 4")

# This code is contributed by vikkycirus
