# Python3 implementation to find
# LIS in circular way Utility
# function to find LIS using
# Dynamic programmi
def computeLIS(circBuff, start, end, n):
    LIS = [0 for i in range(end)]

    # Initialize LIS values
    # for all indexes
    for i in range(start, end):
        LIS[i] = 1

    # Compute optimized LIS values
    # in bottom up manner
    for i in range(start + 1, end):

        # Set j on the basis of current
        # window i.e. first element of
        # the current window
        for j in range(start, i):
            if (circBuff[i] > circBuff[j] and
                    LIS[i] < LIS[j] + 1):
                LIS[i] = LIS[j] + 1

    # Pick maximum of all LIS values
    res = -100000
    for i in range(start, end):
        res = max(res, LIS[i])
    return res


# Function to find Longest Increasing
# subsequence in Circular manner
def LICS(arr, n):
    # Make a copy of given
    # array by appending same
    # array elements to itself
    circBuff = [0 for i in range(2 * n)]
    for i in range(n):
        circBuff[i] = arr[i]
    for i in range(n, 2 * n):
        circBuff[i] = arr[i - n]

    # Perform LIS for each
    # window of size n
    res = -100000
    for i in range(n):
        res = max(computeLIS(circBuff, i,
                             i + n, n), res)
    return res


# Driver code
arr = [1, 4, 6, 2, 3]
n = len(arr)
print("Length of LICS is", LICS(arr, n))
