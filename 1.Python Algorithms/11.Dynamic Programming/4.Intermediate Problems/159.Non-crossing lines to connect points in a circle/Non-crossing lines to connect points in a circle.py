# Python3 program to count number
# of ways to connect n (where n
# is even) points on a circle such
# that no two connecting lines
# cross each other and every point
# is connected with one other point.

# A dynamic programming based
# function to find nth Catalan number
def catalanDP(n):
    # Table to store results
    # of subproblems
    catalan = [1 for i in range(n + 1)]

    # Fill entries in catalan[]
    # using recursive formula
    for i in range(2, n + 1):
        catalan[i] = 0
        for j in range(i):
            catalan[i] += (catalan[j] *
                           catalan[i - j - 1])
    # Return last entry
    return catalan[n]


# Returns count of ways to connect
# n points on a circle such that
# no two connecting lines cross
# each other and every point is
# connected with one other point.
def countWays(n):
    # Throw error if n is odd
    if (n & 1):
        print("Invalid")
        return 0

    # Else return n/2'th Catalan number
    return catalanDP(n // 2)


# Driver Code
print(countWays(6))
