# Python3 program to find Maximum decimal
# value Path in
# Binary matrix

N = 4


# Returns maximum decimal value in binary matrix.
# Here p indicate power of 2
def MaximumDecimalValue(mat, n):
    dp = [[0 for i in range(n)] for i in range(n)]
    if (mat[0][0] == 1):
        dp[0][0] = 1  # 1*(2^0)

    # Compute binary stream of first row of matrix
    # and store result in dp[0][i]
    for i in range(1, n):

        # indicate 1*(2^i) + result of previous
        if (mat[0][i] == 1):
            dp[0][i] = dp[0][i - 1] + 2 ** i

        # indicate 0*(2^i) + result of previous
        else:
            dp[0][i] = dp[0][i - 1]

    # Compute binary stream of first column of matrix
    # and store result in dp[i][0]
    for i in range(1, n):

        # indicate 1*(2^i) + result of previous
        if (mat[i][0] == 1):
            dp[i][0] = dp[i - 1][0] + 2 ** i

    # indicate 0*(2^i) + result of previous
    else:
        dp[i][0] = dp[i - 1][0]

    # Traversal rest Binary matrix and Compute maximum
    # decimal value
    for i in range(1, n):
        for j in range(1, n):

            # Here (i+j) indicate the current power of
            # 2 in path that is 2^(i+j)
            if (mat[i][j] == 1):
                dp[i][j] = max(dp[i][j - 1], dp[i - 1][j]) + (2 ** (i + j))
            else:
                dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])

    # Return maximum decimal value in binary matrix
    return dp[n - 1][n - 1]


# Driver program
if __name__ == '__main__':
    mat = [[1, 1, 0, 1],
           [0, 1, 1, 0],
           [1, 0, 0, 1],
           [1, 0, 1, 1]]

    print(MaximumDecimalValue(mat, 4))
