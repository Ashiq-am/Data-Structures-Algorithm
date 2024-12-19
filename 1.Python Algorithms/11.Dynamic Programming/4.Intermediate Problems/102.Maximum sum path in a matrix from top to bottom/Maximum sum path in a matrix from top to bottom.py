# Python3 implementation to find
# the maximum sum path in a matrix

SIZE = 10
INT_MIN = -10000000


# function to find the maximum sum
# path in a matric
def maxSum(mat, n):
    # if there is a single elementif
    # there is a single element only only
    if n == 1:
        return mat[0][0]

    # dp[][] matrix to store the results
    # of each iteration
    dp = [[0 for i in range(n)] for i in range(n)]
    maxSum = INT_MIN

    # base case, copying elements of
    # last row
    for j in range(n):
        dp[n - 1][j] = mat[n - 1][j]

    # building up the dp[][] matrix from
    # bottom to the top row
    for i in range(n - 2, -1, -1):
        for j in range(n):
            maxi = INT_MIN

            # finding the maximum diagonal
            # element in the
            # (i+1)th row if that cell exists
            if ((((j - 1) >= 0) and
                 (maxi < dp[i + 1][j - 1]))):
                maxi = dp[i + 1][j - 1]
            if ((((j + 1) < n) and
                 (maxi < dp[i + 1][j + 1]))):
                maxi = dp[i + 1][j + 1]

            # adding that 'max' element to the
            # mat[i][j] element
            dp[i][j] = mat[i][j] + maxi

    # finding the maximum value from the
    # first row of dp[][]
    for j in range(n):
        if (maxSum < dp[0][j]):
            maxSum = dp[0][j]

    # required maximum sum
    return maxSum


# Driver program to test above
if __name__ == '__main__':
    mat = [[5, 6, 1, 7],
           [-2, 10, 8, -1],
           [3, -7, -9, 11],
           [12, -4, 2, 6]]

    n = 4
    print("Maximum Sum=", maxSum(mat, n))


