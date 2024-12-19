#Python3 program to reverse bits using lookup table.

# Lookup table that store the reverse of each table
lookuptable = []

# Generate a lookup table for 32bit operating system
# using macro
def R2(n):
	return lookuptable.extend([n,	 n + 2*64,	 n + 1*64,	 n + 3*64])

def R4(n):
	return R2(n), R2(n + 2*16), R2(n + 1*16), R2(n + 3*16)

def R6(n):
	return R4(n), R4(n + 2*4 ), R4(n + 1*4 ), R4(n + 3*4 )

lookuptable.extend([R6(0), R6(2), R6(1), R6(3)])

# Function to reverse bits of num
def reverseBits(num):

	reverse_num = 0

	# Reverse and then rearrange

	# first chunk of 8 bits from right
	reverse_num = lookuptable[num & 0xff ]<<24 | lookuptable[ (num >> 8) & 0xff ]<<16 |lookuptable[ (num >> 16 )& 0xff ]<< 8 | lookuptable[ (num >>24 ) & 0xff ]

	return reverse_num

# Driver program to test above function
x = 12456
print(reverseBits(x))


#This code is contributed by phasing17
