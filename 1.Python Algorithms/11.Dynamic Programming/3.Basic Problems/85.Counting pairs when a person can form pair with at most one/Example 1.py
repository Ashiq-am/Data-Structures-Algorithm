# Python program to find Number of ways
# in which participant can take part.

# Function to calculate number of ways.
def numberOfWays(x):
    # Base condition
    if x == 0 or x == 1:
        return 1

    # A participant can choose to consider
    # (1) Remains single. Number of people
    # reduce to (x-1)
    # (2) Pairs with one of the (x-1) others.
    # For every pairing, number of people
    # reduce to (x-2).
    else:
        return (numberOfWays(x - 1) +
                (x - 1) * numberOfWays(x - 2))


# Driver code
x = 3
print(numberOfWays(x))
