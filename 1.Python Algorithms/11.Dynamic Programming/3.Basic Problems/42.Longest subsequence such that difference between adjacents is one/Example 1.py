# Function to find the length of longest subsequence
def longestSubseqWithDiffOne(arr, n):
    # Initialize the dp[] array with 1 as a
    # single element will be of 1 length
    dp = [1 for i in range(n)]

    # Start traversing the given array
    for i in range(n):
        # Compare with all the previous elements
        for j in range(i):
            # If the element is consecutive then
            # consider this subsequence and update
            # dp[i] if required.
            if ((arr[i] == arr[j] + 1) or (arr[i] == arr[j] - 1)):
                dp[i] = max(dp[i], dp[j] + 1)

    # Longest length will be the maximum value
    # of dp array.
    result = 1
    for i in range(n):
        if (result < dp[i]):
            result = dp[i]

    return result


# Driver code
arr = [1, 2, 3, 4, 5, 3, 2]
# Longest subsequence with one difference is
# {1, 2, 3, 4, 3, 2}
n = len(arr)
print
longestSubseqWithDiffOne(arr, n)
