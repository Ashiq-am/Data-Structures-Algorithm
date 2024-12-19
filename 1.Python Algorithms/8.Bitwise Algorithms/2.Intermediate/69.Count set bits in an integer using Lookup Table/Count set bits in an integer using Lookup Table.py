# Python3 count to count number of set bits
# using lookup table in O(1) time

# Generate a lookup table for 32 bit integers

lookuptable = []


def B2(n):
	lookuptable.extend([n, n + 1, n + 1, n + 2])


def B4(n):
	B2(n), B2(n + 1), B2(n + 1), B2(n + 2)


def B6(n):
	B4(n), B4(n + 1), B4(n + 1), B4(n + 2)


# Lookup table that store the reverse of each table
lookuptable.extend([B6(0), B6(1), B6(1), B6(2)])

# function countset Bits Using lookup table
# ans return set bits count


def countSetBits(N):

	# adding the bits in chunks of 8 bits
	count = lookuptable[N & 0xff] + lookuptable[(N >> 8) & 0xff] + lookuptable[(
		N >> 16) & 0xff] + lookuptable[(N >> 24) & 0xff]
	return count


# Driver Code
N = 354

# Function Call
print(countSetBits(N))


# This code is contributed by phasing17
