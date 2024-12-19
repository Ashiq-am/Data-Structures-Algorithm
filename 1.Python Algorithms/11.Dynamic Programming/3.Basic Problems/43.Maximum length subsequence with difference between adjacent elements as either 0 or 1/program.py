# Python implementation to find maximum length
# subsequence with difference between adjacent
# elements as either 0 or 1

# function to find maximum length subsequence
# with difference between adjacent elements as
# either 0 or 1
def maxLenSub(arr, n):
    mls = []
    max = 0

    # Initialize mls[] values for all indexes
    for i in range(n):
        mls.append(1)

    # Compute optimized maximum length subsequence
    # values in bottom up manner
    for i in range(n):
        for j in range(i):
            if (abs(arr[i] - arr[j]) <= 1 and mls[i] < mls[j] + 1):
                mls[i] = mls[j] + 1

    # Store maximum of all 'mls' values in 'max'
    for i in range(n):
        if (max < mls[i]):
            max = mls[i]

    # required maximum length subsequence
    return max


# Driver program to test above
arr = [2, 5, 6, 3, 7, 6, 5, 8]
n = len(arr)
print("Maximum length subsequence = ", maxLenSub(arr, n))

# This code is contributed by "Abhishek Sharma 44"
