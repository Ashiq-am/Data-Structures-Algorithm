# Python implementation to
# count number of ways to
# tile a floor of size n x m
# using 1 x m tiles

def countWays(n, m):
    # table to store values
    # of subproblems
    count = []
    for i in range(n + 2):
        count.append(0)
    count[0] = 0

    # Fill the table upto value n
    for i in range(1, n + 1):

        # recurrence relation
        if (i > m):
            count[i] = count[i - 1] + count[i - m]

        # base cases
        elif (i < m or i == 1):
            count[i] = 1

        # i = = m
        else:
            count[i] = 2

    # required number of ways
    return count[n]


# Driver code

n = 7
m = 4

print("Number of ways = ", countWays(n, m))