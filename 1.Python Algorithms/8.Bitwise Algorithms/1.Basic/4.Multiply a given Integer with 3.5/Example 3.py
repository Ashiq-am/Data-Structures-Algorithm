# Python3 program for the above approach

# Function to multiple number
# with 3.5
def multiplyWith3Point5(x):
	r = 0

	# The 3.5 is 7/2, so multiply
	# by 7 (x * 7) then
	# divide the result by 2
	# (result/2) x * 7 -> 7 is
	# 0111 so by doing multiply
	# by 7 it means we do 2
	# shifting for the number
	# but since we doing
	# multiply we need to take
	# care of carry one.
	x1Shift = x << 1
	x2Shifts = x << 2

	r = (x ^ x1Shift) ^ x2Shifts
	c = (x & x1Shift) | (x & x2Shifts) | (x1Shift & x2Shifts)
	while (c > 0):
		c <<= 1
		t = r
		r ^= c
		c &= t

	# Then divide by 2
	# r / 2
	r = r >> 1
	return r

# Driver Code
if __name__ == '__main__':
	print(multiplyWith3Point5(5))

# This code is contributed by nirajgusain5
