# Python3 program to implement the approach

# Function to build DFA for divisor k


def preprocess(k, Table):

	# The following loop calculates the
	# two transitions for each state,
	# starting from state 0
	for state in range(k):

		# Calculate next state for bit 0
		trans0 = state << 1
		if (trans0 < k):
			Table[state][0] = trans0
		else:
			Table[state][0] = trans0 - k

		# Calculate next state for bit 1
		trans1 = (state << 1) + 1

		if trans1 < k:
			Table[state][1] = trans1
		else:
			Table[state][1] = trans1 - k


# A recursive utility function that
# takes a 'num' and DFA (transition
# table) as input and process 'num'
# bit by bit over DFA
def isDivisibleUtil(num, state, Table):
	# process "num" bit by bit
	# from MSB to LSB
	if (num != 0):
		state = isDivisibleUtil(num >> 1, state, Table)
		state = Table[state][num & 1]
	return state


# The main function that divides 'num'
# by k and returns the remainder
def isDivisible(num, k):

	# Allocate memory for transition table.
	# The table will have k*2 entries
	Table = [None for i in range(k)]
	for i in range(k):
		Table[i] = [0, 0]

	# Fill the transition table
	preprocess(k, Table)

	# Process ‘num’ over DFA and
	# get the remainder
	state = 0
	state = isDivisibleUtil(num, state, Table)

	# Note that the final value
	# of state is the remainder
	return state


# Driver Code

num = 47 # Number to be divided
k = 5 # Divisor

remainder = isDivisible(num, k)

if (remainder == 0):
	print("Divisible")
else:
	print("Not Divisible: Remainder is", remainder)


# This is code contributed by phasing17
