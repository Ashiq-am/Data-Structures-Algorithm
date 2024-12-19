# Python3 program to find the path
# having the maximum weight in matrix

MAX = 1000


# Function which return the
# maximum weight path sum
def maxCost(mat, N):
    # creat 2D matrix to store the sum of the path
    dp = [[0 for i in range(N)] for j in range(N)]

    dp[0][0] = mat[0][0]

    # Initialize first column of total weight
    # array (dp[i to N][0])
    for i in range(1, N):
        dp[i][0] = mat[i][0] + dp[i - 1][0]

    # Calculate rest path sum of weight matrix
    for i in range(1, N):
        for j in range(1, min(i + 1, N)):
            dp[i][j] = mat[i][j] + \
                       max(dp[i - 1][j - 1],
                           dp[i - 1][j])

    # find the max weight path sum to reach
    # the last row
    result = 0
    for i in range(N):
        if (result < dp[N - 1][i]):
            result = dp[N - 1][i]

    # return maximum weight path sum
    return result


# Driver Program

mat = [[4, 1, 5, 6, 1],
       [2, 9, 2, 11, 10],
       [15, 1, 3, 15, 2],
       [16, 92, 41, 4, 3],
       [8, 142, 6, 4, 8]]

N = 5
print('Maximum Path Sum :', maxCost(mat, N))
