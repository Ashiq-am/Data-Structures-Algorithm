# python program to get total xor
# of all subarray xors

# Returns XOR of all subarray xors
def getTotalXorOfSubarrayXors(arr, N):
    # initialize result by 0 as
    # (a xor 0 = a)
    res = 0

    # select the starting element
    for i in range(0, N):

        # select the eNding element
        for j in range(i, N):

            # Do XOR of elements in
            # current subarray
            for k in range(i, j + 1):
                res = res ^ arr[k]

    return res


# Driver code to test above methods
arr = [3, 5, 2, 4, 6]
N = len(arr)

print(getTotalXorOfSubarrayXors(arr, N))

# This code is contributed by Sam007.
