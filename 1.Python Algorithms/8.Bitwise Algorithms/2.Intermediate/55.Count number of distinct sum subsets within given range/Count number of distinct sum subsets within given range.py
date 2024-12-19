# Python3 Program to count the number
# distinct values of sum of some
# subset in a range

# Constant size for bitset
SZ = 100001

def countOfpossibleNumbers(S, N, L, R):

	# Initially BS is 1
	BS = 1

	for i in range(N):

		# Left shift the bitset for each
		# element and taking bitwise OR
		# with previous bitset
		BS = BS | (BS << S[i])

	# Convert BS to bitset array
	BS = bin(BS)[2::]
	BS = [int(i) for i in BS.zfill(SZ)][::-1]

	# Initializing the prefix array to zero
	prefix = [0 for i in range(SZ)]

	# Build the prefix array
	for i in range(1, SZ):
		prefix[i] = prefix[i - 1] + BS[i]

	# Answer the given query
	ans = prefix[R] - prefix[L - 1]

	return ans

# Driver Code to test above functions
S = [1, 2, 3, 5, 7]
N = len(S)
L, R = 1, 18

print(countOfpossibleNumbers(S, N, L, R))

# This code is contributed by phasing17
