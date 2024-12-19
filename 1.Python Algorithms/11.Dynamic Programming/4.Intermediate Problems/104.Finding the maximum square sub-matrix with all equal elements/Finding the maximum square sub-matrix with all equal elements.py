# Python 3 program to find
# maximum K such that K x K
# is a submatrix with equal
# elements.
Row = 6
Col = 6


# Returns size of the
# largest square sub-matrix
# with all same elements.
def largestKSubmatrix(a):
    dp = [[0 for x in range(Row)]
          for y in range(Col)]

    result = 0
    for i in range(Row):
        for j in range(Col):

            # If elements is at top
            # row or first column,
            # it wont form a square
            # matrix's bottom-right
            if (i == 0 or j == 0):
                dp[i][j] = 1

            else:

                # Check if adjacent
                # elements are equal
                if (a[i][j] == a[i - 1][j] and
                        a[i][j] == a[i][j - 1] and
                        a[i][j] == a[i - 1][j - 1]):

                    dp[i][j] = min(min(dp[i - 1][j],
                                       dp[i][j - 1]),
                                   dp[i - 1][j - 1]) + 1

                # If not equal, then
                # it will form a 1x1
                # submatrix
                else:
                    dp[i][j] = 1

            # Update result at each (i,j)
            result = max(result, dp[i][j])

    return result


# Driver Code
a = [[2, 2, 3, 3, 4, 4],
     [5, 5, 7, 7, 7, 4],
     [1, 2, 7, 7, 7, 4],
     [4, 4, 7, 7, 7, 4],
     [5, 5, 5, 1, 2, 7],
     [8, 7, 9, 4, 4, 4]]

print(largestKSubmatrix(a))


