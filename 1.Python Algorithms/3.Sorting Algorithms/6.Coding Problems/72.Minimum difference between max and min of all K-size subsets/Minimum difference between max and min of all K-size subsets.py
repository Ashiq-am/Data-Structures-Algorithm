# Python3 program to find minimum
# difference between max and min
# of all subset of K size

# Returns min difference between max
# and min of any K-size subset
def minDifferenceAmongMaxMin(arr, N, K):
    # sort the array so that close
    # elements come together.
    arr.sort()

    # initialize result by a
    # big integer number
    res = 2147483647

    # loop over first (N - K) elements
    # of the array only
    for i in range((N - K) + 1):
        # get difference between max and min
        # of current K-sized segment
        curSeqDiff = arr[i + K - 1] - arr[i]
        res = min(res, curSeqDiff)

    return res


# Driver Code
arr = [10, 20, 30, 100, 101, 102]
N = len(arr)
K = 3
print(minDifferenceAmongMaxMin(arr, N, K))
