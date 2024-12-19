# Python3 program to get the parity of the
# binary representation of a number
nibble_to_bits = [0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2, 3, 2, 3, 3, 4]

# Function to recursively get the nibble
# of a given number and map them in the array
def countSetBits(num):
	nibble = 0
	if (0 == num):
		return nibble_to_bits[0]

	# Find last nibble
	nibble = num & 0xf

	# Use pre-stored values to find count
	# in last nibble plus recursively add
	# remaining nibbles.
	return nibble_to_bits[nibble] + countSetBits(num >> 4)

# Function to get the parity of a number
def getParity(num):
	return countSetBits(num) % 2

# Driver code
n = 7

# Function call
print("Parity of no", n, " = ", ["even", "odd"][getParity(n)])

# This code is contributed by phasing17
