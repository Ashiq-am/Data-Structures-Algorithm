# Python program to demonstrate Integer.bitCount()

def bitsoncount(i):
	assert 0 <= i < 0x100000000
	i = i - ((i >> 1) & 0x55555555)
	i = (i & 0x33333333) + ((i >> 2) & 0x33333333)
	return (((i + (i >> 4) & 0xF0F0F0F) * 0x1010101) & 0xffffffff) >> 24

# Driver code
if __name__ == '__main__':
	x = 4;
	y = 15;
	print(bitsoncount(x));
	print(bitsoncount(y));

# This code is contributed by umadevi9616
