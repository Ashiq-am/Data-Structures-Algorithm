# Function to Count total set bits in all numbers
# from 1 to n


#Get the sum of all set bits
#in the range [1, n]
def countSetBitAll(n):
	# map count function on each number
	print(sum(map(lambda x: bin(x).count("1"), range(1, n + 1))))


# Driver program
n = 8

#Function Call
countSetBitAll(n)


#This code is contributed by phasing17
