# Python3 program to check
# if given number is
# power of 4 or not
def isPowerOfFour(n):
	return (n != 0 and
		((n & (n - 1)) == 0) and
			not(n & 0xAAAAAAAA));

# Driver code
test_no = 64;
if(isPowerOfFour(test_no)):
	print(test_no ,"is a power of 4");
else:
	print(test_no , "is not a power of 4");

# This code contributed by Rajput-Ji
