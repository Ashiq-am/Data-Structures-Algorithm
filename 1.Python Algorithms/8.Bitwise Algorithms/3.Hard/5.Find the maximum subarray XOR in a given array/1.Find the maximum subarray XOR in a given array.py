# A simple Python program
# to find max subarray XOR

def maxSubarrayXOR(arr, n):
    ans = -2147483648  # Initialize result

    # Pick starting points of subarrays
    for i in range(n):

        # to store xor of current subarray
        curr_xor = 0

        # Pick ending points of
        # subarrays starting with i
        for j in range(i, n):
            curr_xor = curr_xor ^ arr[j]
            ans = max(ans, curr_xor)

    return ans


# Driver code

arr = [8, 1, 2, 12]
n = len(arr)

print("Max subarray XOR is ",
      maxSubarrayXOR(arr, n))

# This code is contributed
# by Anant Agarwal.
