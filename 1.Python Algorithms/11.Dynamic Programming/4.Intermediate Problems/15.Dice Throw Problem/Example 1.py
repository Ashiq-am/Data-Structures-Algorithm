# Python3 program to find the number of ways to get sum 'x' with 'n' dice
# where every dice has 'm' faces

# The main function that returns number of ways to get sum 'x'
# with 'n' dice and 'm' with m faces.
def findWays(m, n, x):
    # Create a table to store results of subproblems. One extra
    # row and column are used for simpilicity (Number of dice
    # is directly used as row index and sum is directly used
    # as column index). The entries in 0th row and 0th column
    # are never used.
    table = [[0] * (x + 1) for i in range(n + 1)]  # Initialize all entries as 0

    for j in range(1, min(m + 1, x + 1)):  # Table entries for only one dice
        table[1][j] = 1

    # Fill rest of the entries in table using recursive relation
    # i: number of dice, j: sum
    for i in range(2, n + 1):
        for j in range(1, x + 1):
            for k in range(1, min(m + 1, j)):
                table[i][j] += table[i - 1][j - k]

    # print(dt)
    # Uncomment above line to see content of table

    return table[-1][-1]


# Driver code
print(findWays(4, 2, 1))
print(findWays(2, 2, 3))
print(findWays(6, 3, 8))
print(findWays(4, 2, 5))
print(findWays(4, 3, 5))
