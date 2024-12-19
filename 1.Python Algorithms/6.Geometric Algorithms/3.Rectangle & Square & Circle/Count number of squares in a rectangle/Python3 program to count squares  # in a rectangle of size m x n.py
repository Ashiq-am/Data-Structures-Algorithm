# Python3 program to count squares
# in a rectangle of size m x n

# Returns count of all squares
# in a rectangle of size m x n
def countSquares(m, n):
    # If n is smaller, swap m and n
    if (n < m):
        temp = m
        m = n
        n = temp

    # Now n is greater dimension,
    # apply formula
    return n * (n + 1) * (3 * m - n + 1) // 6


# Driver Code
if __name__ == '__main__':
    m = 4
    n = 3
    print("Count of squares is",
          countSquares(m, n))

# This code is contributed by AnkitRai01
