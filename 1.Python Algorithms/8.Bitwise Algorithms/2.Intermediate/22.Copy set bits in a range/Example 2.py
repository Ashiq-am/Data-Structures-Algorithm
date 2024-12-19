# Python program to copy set bits in a given
# range [l, r] from y to x.

# Copy set bits in range [l, r] from y to x.
# Note that x is passed by reference and modified
# by this function.
def copySetBits(x, y, l, r):

	# l and r must be between 1 to 32
	if (l < 1 or r > 32):
		return x;

	# get the length of the mask
	maskLength = (int) ((1 << (r - l + 1)) - 1);

	# Shift the mask to the required position
	# "&" with y to get the set bits at between
	# l ad r in y
	mask = ((maskLength) << (l - 1)) & y;
	x = x | mask;
	return x;

# Driver code
if __name__ == '__main__':
	x = 10;
	y = 13;
	l = 2;
	r = 3;
	x = copySetBits(x, y, l, r);
	print("Modified x is " , x);

# This code is contributed by gauravrajput1
