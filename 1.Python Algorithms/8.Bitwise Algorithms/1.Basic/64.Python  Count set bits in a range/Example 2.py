# Function to count set bits in a range

def countSetBits(n, l, r):

	# convert n into its binary form
		# using bin()
	# and then process it using string
	# slice methods
	binary = bin(n)[-1:1:-1]

	# count all set bit '1' starting from index l-1
	# to r, where r is exclusive
	print(binary[l - 1: r].count("1"))


# Driver Code
n = 42
l = 2
r = 5
countSetBits(n, l, r)


#This code is contributed by phasing17
