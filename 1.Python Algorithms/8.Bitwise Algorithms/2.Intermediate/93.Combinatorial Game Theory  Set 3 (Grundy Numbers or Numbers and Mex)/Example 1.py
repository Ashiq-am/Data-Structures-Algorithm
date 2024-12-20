''' A recursive Python3 program to find Grundy Number for
a game which is like a one-pile version of Nim.
Game Description : The game starts with a pile of n stones,
and the player to move may take any positive number of stones.
The last player to move wins. Which player wins the game? '''

# A Function to calculate Mex of all the values in
# that set.
def calculateMex(Set):
	Mex = 0

	while (Mex in Set):
		Mex += 1

	return (Mex)

# A function to Compute Grundy Number of 'n'
# Only this function varies according to the game
def calculateGrundy( n):
	if (n == 0):
		return (0)

	Set = set() # A Hash Table

	for i in range(n):
		Set.add(calculateGrundy(i));

	return (calculateMex(Set))

# Driver program to test above functions
n = 10;
print(calculateGrundy(n))

# This code is contributed by ANKITKUMAR34
