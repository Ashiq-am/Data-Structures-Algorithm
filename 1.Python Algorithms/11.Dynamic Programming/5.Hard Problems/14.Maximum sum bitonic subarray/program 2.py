# Python3 implementation to find the
# maximum sum bitonic subarray

# Function to find the maximum sum bitonic
# subarray.
def maxSumBitonicSubArr(arr, n):
    # to store the maximum sum
    # bitonic subarray
    max_sum = -10 ** 9

    i = 0
    while (i < n):

        # Find the longest increasing subarray
        # starting at i.
        j = i
        while (j + 1 < n and arr[j] < arr[j + 1]):
            j += 1

        # Now we know that a[i..j] is an
        # increasing subarray. Remove non-
        # positive elements from the left
        # side as much as possible.
        while (i < j and arr[i] <= 0):
            i += 1

        # Find the longest decreasing subarray
        # starting at j.
        k = j
        while (k + 1 < n and arr[k] > arr[k + 1]):
            k += 1

        # Now we know that a[j..k] is a
        # decreasing subarray. Remove non-
        # positive elements from the right
        # side as much as possible.
        # last is needed to keep the last
        # seen element.
        last = k
        while (k > j and arr[k] <= 0):
            k -= 1

        # Compute the max sum of the
        # increasing part.
        nn = arr[i:j + 1]
        sum_inc = sum(nn)

        # Compute the max sum of the
        # decreasing part.
        nn = arr[j:k + 1]
        sum_dec = sum(nn)

        # The overall max sum is the sum of
        # both parts minus the peak element,
        # because it was counted twice.
        sum_all = sum_inc + sum_dec - arr[j]

        max_sum = max([max_sum, sum_inc,
                       sum_dec, sum_all])

        # If the next element is equal to the
        # current, i.e. arr[i+1] == arr[i],
        # last == i.
        # To ensure the algorithm has progress,
        # get the max of last and i+1.
        i = max(last, i + 1)

    # required maximum sum
    return max_sum


# Driver Code

# The example from the article, the
# answer is 19.
arr = [5, 3, 9, 2, 7, 6, 4]
n = len(arr)
print("Maximum Sum = ",
      maxSumBitonicSubArr(arr, n))

# Always increasing, the answer is 15.
arr2 = [1, 2, 3, 4, 5]
n2 = len(arr2)
print("Maximum Sum = ",
      maxSumBitonicSubArr(arr2, n2))

# Always decreasing, the answer is 15.
arr3 = [5, 4, 3, 2, 1]
n3 = len(arr3)
print("Maximum Sum = ",
      maxSumBitonicSubArr(arr3, n3))

# All are equal, the answer is 5.
arr4 = [5, 5, 5, 5]
n4 = len(arr4)
print("Maximum Sum = ",
      maxSumBitonicSubArr(arr4, n4))

# The whole array is bitonic,
# but the answer is 7.
arr5 = [-1, 0, 1, 2, 3, 1, 0, -1, -10]
n5 = len(arr5)
print("Maximum Sum = ",
      maxSumBitonicSubArr(arr5, n5))

# The answer is 4 (the tail).
arr6 = [-1, 0, 1, 2, 0, -1, -2, 0, 1, 3]
n6 = len(arr6)
print("Maximum Sum = ",
      maxSumBitonicSubArr(arr6, n6))

