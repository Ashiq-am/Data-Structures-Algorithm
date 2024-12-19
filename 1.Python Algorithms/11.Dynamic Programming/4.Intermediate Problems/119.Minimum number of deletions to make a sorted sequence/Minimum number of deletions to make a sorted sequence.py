# Python3 implementation to find
# minimum number of deletions to
# make a sorted sequence

# lis() returns the length
# of the longest increasing
# subsequence in arr[] of size n
def lis(arr, n):
    result = 0
    lis = [0 for i in range(n)]

    # Initialize LIS values
    # for all indexes
    for i in range(n):
        lis[i] = 1

    # Compute optimized LIS values
    # in bottom up manner
    for i in range(1, n):
        for j in range(i):
            if (arr[i] > arr[j] and
                    lis[i] < lis[j] + 1):
                lis[i] = lis[j] + 1

    # Pick resultimum
    # of all LIS values
    for i in range(n):
        if (result < lis[i]):
            result = lis[i]

    return result


# Function to calculate minimum
# number of deletions
def minimumNumberOfDeletions(arr, n):
    # Find longest increasing
    # subsequence
    len = lis(arr, n)

    # After removing elements
    # other than the lis, we
    # get sorted sequence.
    return (n - len)


# Driver Code
arr = [30, 40, 2, 5, 1,
       7, 45, 50, 8]
n = len(arr)
print("Minimum number of deletions = ",
      minimumNumberOfDeletions(arr, n))
