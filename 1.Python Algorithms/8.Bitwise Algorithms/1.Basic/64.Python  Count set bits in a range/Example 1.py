# Function to count set bits in a range

def countSetBits(n,l,r):

	# convert n into it's binary
	binary = bin(n)

	# remove first two characters
	binary = binary[2:]

	# reverse string
	binary = binary[-1::-1]

	# count all set bit '1' starting from index l-1
	# to r, where r is exclusive
	print (len([binary[i] for i in range(l-1,r) if binary[i]=='1']))

# Driver program
if __name__ == "__main__":
	n=42
	l=2
	r=5
	countSetBits(n,l,r)
