# Python3 program to get total
# xor of all subarray xors

# Returns XOR of all
# subarray xors
def getTotalXorOfSubarrayXors(arr, N):
    # initialize result by 0
    # as (a XOR 0 = a)
    res = 0

    # loop over all elements once
    for i in range(0, N):

        # get the frequency of
        # current element
        freq = (i + 1) * (N - i)

        # Uncomment below line to print
        # the frequency of arr[i]

        # if frequency is odd, then
        # include it in the result
        if (freq % 2 == 1):
            res = res ^ arr[i]

    # return the result
    return res


# Driver Code
arr = [3, 5, 2, 4, 6]
N = len(arr)
print(getTotalXorOfSubarrayXors(arr, N))

# This code is contributed
# by Smitha
