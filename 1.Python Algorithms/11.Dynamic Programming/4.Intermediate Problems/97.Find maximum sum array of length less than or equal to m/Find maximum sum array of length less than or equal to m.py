# A Dynamic Programming based Python3
# program to find maximum sum of array
# of size less than or equal to m from
# given n arrays

# N and M to define sizes of arr,
# dp, current_arr and maxSum
N = 105
M = 1001

# INF to define min value
INF = -1111111111


# Function to find maximum sum
def maxSum(arr):
    # dp array of size N x M
    dp = [[-1 for x in range(M)]
          for y in range(N)]

    # current_arr of size M
    current_arr = [0] * M

    # maxsum of size M
    maxsum = [0] * M

    current_arr[0] = 0

    # If we have 0 elements
    # from 0th array
    dp[0][0] = 0

    for i in range(1, 6):
        len = arr[i - 1][0]

        # Compute the cumulative sum array
        for j in range(1, len + 1):
            current_arr[j] = arr[i - 1][j]
            current_arr[j] += current_arr[j - 1]
            maxsum[j] = INF

        # Calculating the maximum contiguous
        # array for every length j, j is from
        # 1 to lengtn of the array
        j = 1
        while j <= len and j <= 6:
            for k in range(1, len + 1):
                if (j + k - 1 <= len):
                    maxsum[j] = max(maxsum[j],
                                    current_arr[j + k - 1] -
                                    current_arr[k - 1])

            j += 1

        # Every state is depending on
        # its previous state
        for j in range(7):
            dp[i][j] = dp[i - 1][j]

        # computation of dp table similar
        # approach as knapsack problem
        for j in range(1, 7):
            cur = 1
            while cur <= j and cur <= len:
                dp[i][j] = max(dp[i][j],
                               dp[i - 1][j - cur] +
                               maxsum[cur])

                cur += 1

    # Now we have done processing with
    # the last array lets find out
    # what is the maximum sum possible
    ans = 0
    for i in range(7):
        ans = max(ans, dp[5][i])

    return ans


# Driver code
if __name__ == "__main__":
    # First element of each
    # row is the size of that row
    arr = [[3, 2, 3, 5],
           [2, 7, -1],
           [2, 8, 10],
           [4, 5, 2, 6, 1],
           [3, 2, 3, -2]]

    print("Maximum sum can be obtained","is : ", maxSum(arr))
