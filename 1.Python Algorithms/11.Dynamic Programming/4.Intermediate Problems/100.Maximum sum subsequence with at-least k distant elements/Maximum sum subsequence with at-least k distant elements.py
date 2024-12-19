# Python3 program to find maximum
# sum subsequence such that elements
# are at least k distance away.

def maxSum(arr, N, k):
    # MS[i] is going to store maximum sum
    # subsequence in subarray from arr[i]
    # to arr[n-1]
    MS = [0 for i in range(N)]

    # We fill MS from right to left.
    MS[N - 1] = arr[N - 1]
    for i in range(N - 2, -1, -1):
        if (i + k + 1 >= N):
            MS[i] = max(arr[i], MS[i + 1])
        else:
            MS[i] = max(arr[i] + MS[i + k + 1],
                        MS[i + 1])

    return MS[0]


# Driver code
N = 10
k = 2
arr = [50, 70, 40, 50, 90, 70, 60, 40, 70, 50]
print(maxSum(arr, N, k))


