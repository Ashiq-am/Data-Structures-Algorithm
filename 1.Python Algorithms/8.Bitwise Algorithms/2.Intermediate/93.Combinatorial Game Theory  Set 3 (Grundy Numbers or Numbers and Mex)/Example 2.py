# A recursive Python3 program to find Grundy Number
# for a game which is one-pile version of Nim.
# Game Description : The game starts with a pile
# of n stones, and the player to move may take
# any positive number of stones up to 3 only.
# The last player to move wins.


# A function to Compute Grundy Number of 'n'
# Only this function varies according to the game
def calculateGrundy(n):
    if 0 <= n <= 3:
        return n

    else:
        return (n % (3 + 1))


# Driver program to test above functions
if __name__ == "__main__":
    n = 10
    print(calculateGrundy(n))

# This code is contributed by rahulnamdevrn27
