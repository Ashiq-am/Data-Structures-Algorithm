# Python3 program to find maximum pair
# sum whose difference is less than K

# method to return maximum sum we can
# get by get by finding less than K
# difference pair
def maxSumPairWithDifferenceLessThanK(arr, N, K):
    # Sort input array in ascending order.
    arr.sort()

    # dp[i] denotes the maximum disjoint
    # pair sum we can achieve using first
    # i elements
    dp = [0] * N

    # if no element then dp value will be 0
    dp[0] = 0

    for i in range(1, N):

        # first give previous value to
        # dp[i] i.e. no pairing with
        # (i-1)th element
        dp[i] = dp[i - 1]

        # if current and previous element
        # can form a pair
        if (arr[i] - arr[i - 1] < K):

            # update dp[i] by choosing
            # maximum between pairing
            # and not pairing
            if (i >= 2):
                dp[i] = max(dp[i], dp[i - 2] + arr[i] + arr[i - 1]);
            else:
                dp[i] = max(dp[i], arr[i] + arr[i - 1]);

    # last index will have the result
    return dp[N - 1]


# Driver code to test above methods
arr = [3, 5, 10, 15, 17, 12, 9]
N = len(arr)
K = 4
print(maxSumPairWithDifferenceLessThanK(arr, N, K))
