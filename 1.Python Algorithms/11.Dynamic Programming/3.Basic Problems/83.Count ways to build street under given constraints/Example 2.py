# Python3 program of above approach

# Program to count ways
def countways(n):
    A = [0 for i in range(n + 2)]
    A[0] = 1
    A[1] = 3
    A[2] = 7

    # Iterate from 2 to n
    for i in range(2, n + 1):
        A[i] = 2 * A[i - 1] + A[i - 2]

    return A[n]


# Driver code
n = 5

# Count Ways
print(countways(5))
