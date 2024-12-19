# Python3 program to find smallest possible
# length of a string of only three characters

# A memoized function find result recursively.
# a, b and c are counts of 'a's, 'b's and
# 'c's in str
def length(a, b, c):
    global DP

    # print(a, b, c)

    # If this subproblem is already
    # evaluated
    if a < 0 or b < 0 or c < 0:
        return 0

    if (DP[a][b] != -1):
        return DP[a][b]

    # If there is only one type
    # of character
    if (a == 0 and b == 0):
        DP[a][b] = c
        return c
    if (a == 0 and c == 0):
        DP[a][b] = b
        return b
    if (b == 0 and c == 0):
        DP[a][b] = a
        return a

    # If only two types of characters
    # are present
    if (a == 0):
        DP[a][b] = length(a + 1, b - 1,
                          c - 1)
        return DP[a][b]

    if (b == 0):
        DP[a][b] = length(a - 1, b + 1,
                          c - 1)
        return DP[a][b]

    if (c == 0):
        DP[a][b] = length(a - 1, b - 1,
                          c + 1)
        return DP[a][b]

    # If all types of characters are present.
    # Try combining all pairs.
    x = length(a - 1, b - 1, c + 1)
    y = length(a - 1, b + 1, c - 1)
    z = length(a + 1, b - 1, c - 1)

    DP[a][b] = min([x, y, z])

    return DP[a][b]


# Returns smallest possible length with
# given operation allowed.
def stringReduction(str):
    n = len(str)

    # Counting occurrences of three different
    # characters 'a', 'b' and 'c' in str
    count = [0] * 3

    for i in range(n):
        count[ord(str[i]) - ord('a')] += 1

    return length(count[0], count[1], count[2])


# Driver code
if __name__ == '__main__':
    DP = [[[-1 for i in range(110)]
           for i in range(110)]
          for i in range(110)]

    str = "abcbbaacb"

    print(stringReduction(str))

# This code is contributed by mohit kumar 29
