# Python 3 implementation
# to find the maximum sum
# bitonic subarray

# function to find the
# maximum sum bitonic subarray
def maxSumBitonicSubArr(arr, n):
    # 'msis[]' to store the maximum
    # sum increasing subarray up to
    # each index of 'arr' from the
    # beginning 'msds[]' to store
    # the maximum sum decreasing
    # subarray from each index of
    # 'arr' up to the end
    msis = [None] * n
    msds = [None] * n

    # to store the maximum
    # sum bitonic subarray
    max_sum = 0

    # building up the maximum
    # sum increasing subarray
    # for each array index
    msis[0] = arr[0]
    for i in range(1, n):
        if (arr[i] > arr[i - 1]):
            msis[i] = msis[i - 1] + arr[i]
        else:
            msis[i] = arr[i]

            # building up the maximum
    # sum decreasing subarray
    # for each array index
    msds[n - 1] = arr[n - 1]
    for i in range(n - 2, -1, -1):
        if (arr[i] > arr[i + 1]):
            msds[i] = msds[i + 1] + arr[i]
        else:
            msds[i] = arr[i]

    # for each array index,
    # calculating the maximum
    # sum of bitonic subarray
    # of which it is a part of
    for i in range(n):

        # if true , then update
        # 'max' bitonic subarray sum
        if (max_sum < (msis[i] +
                       msds[i] - arr[i])):
            max_sum = (msis[i] +
                       msds[i] - arr[i])

    # required maximum sum
    return max_sum


# Driver Code
arr = [5, 3, 9, 2, 7, 6, 4]
n = len(arr)
print("Maximum Sum = " +
      str(maxSumBitonicSubArr(arr, n)))