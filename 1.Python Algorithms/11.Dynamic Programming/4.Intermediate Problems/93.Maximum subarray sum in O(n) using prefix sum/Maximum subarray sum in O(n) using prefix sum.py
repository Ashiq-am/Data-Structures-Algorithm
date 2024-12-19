# Python3 program to find out
# maximum subarray sum in
# linear time using prefix
# sum.
import math


# Function to compute maximum
# subarray sum in linear time.
def maximumSumSubarray(arr, n):
    # Initialize minimum prefix
    # sum to 0.
    min_prefix_sum = 0

    # Initialize maximum subarray
    # sum so far to -infinity.
    res = -math.inf

    # Initialize and compute the
    # prefix sum array.
    prefix_sum = []
    prefix_sum.append(arr[0])

    for i in range(1, n):
        prefix_sum.append(prefix_sum[i - 1] + arr[i])

    # loop through the array keep
    # track of minimum prefix sum
    # so far and maximum subarray
    # sum.
    for i in range(n):
        res = max(res, prefix_sum[i] - min_prefix_sum)
        min_prefix_sum = min(min_prefix_sum, prefix_sum[i])

    return res


# Driver Program

# Test case 1
arr1 = [-2, -3, 4, -1, -2, 1, 5, -3]
n1 = len(arr1)
print(maximumSumSubarray(arr1, n1))

# Test case 2
arr2 = [4, -8, 9, -4, 1, -8, -1, 6]
n2 = len(arr2)
print(maximumSumSubarray(arr2, n2))
