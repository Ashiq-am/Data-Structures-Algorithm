# An efficient Python3 program to check
# if binary representations of a number
# and it's complement are anagram.
ULL_SIZE = 64

# Returns true if binary representations of
# a and b are anagram.
def bit_anagram_check(a):

	#_popcnt64(a) gives number of 1's present
	# in binary representation of a. If number
	# of 1s is half of total bits, return true.
	return (bin(a).count("1") == (ULL_SIZE >> 1))

# Driver Code
a = 4294967295
print(int(bit_anagram_check(a)))

# This code is contributed by Mohit Kumar
