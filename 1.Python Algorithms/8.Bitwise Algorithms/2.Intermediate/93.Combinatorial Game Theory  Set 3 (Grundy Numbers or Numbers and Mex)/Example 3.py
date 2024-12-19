# A recursive Python3 program to
# find Grundy Number for a game.
# Game Description : The game starts with a number- 'n'
# and the player to move divides the number- 'n' with 2, 3
# or 6 and then take the floor. If the integer becomes 0,
# it is removed. The last player to move wins.

# A Function to calculate Mex
# of all the values in that set.
def calculateMex(Set):
    Mex = 0
    while Mex in Set:
        Mex += 1

    return Mex


# A function to Compute Grundy Number of 'n'
# Only this function varies according to the game
def calculateGrundy(n):
    if n == 0:
        return 0

    Set = set()  # A Hash Table

    Set.add(calculateGrundy(n // 2))
    Set.add(calculateGrundy(n // 3))
    Set.add(calculateGrundy(n // 6))

    return (calculateMex(Set))


# Driver program to test above functions
if __name__ == "__main__":
    n = 10
    print(calculateGrundy(n))

# This code is contributed by Rituraj Jain
