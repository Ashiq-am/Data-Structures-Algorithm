# Python program to find the maximum sum such that
# no three are consecutive

# Returns maximum subsequence sum such that no three
# elements are consecutive
def maxSumWO3Consec(arr, n):
    # Stores result for subarray arr[0..i], i.e.,
    # maximum possible sum in subarray arr[0..i]
    # such that no three elements are consecutive.
    sum = [0 for k in range(n)]

    # Base cases (process first three elements)

    if n >= 1:
        sum[0] = arr[0]

    if n >= 2:
        sum[1] = arr[0] + arr[1]

    if n > 2:
        sum[2] = max(sum[1], max(arr[1] + arr[2], arr[0] + arr[2]))

    # Process rest of the elements
    # We have three cases
    # 1) Exclude arr[i], i.e., sum[i] = sum[i-1]
    # 2) Exclude arr[i-1], i.e., sum[i] = sum[i-2] + arr[i]
    # 3) Exclude arr[i-2], i.e., sum[i-3] + arr[i] + arr[i-1]
    for i in range(3, n):
        sum[i] = max(max(sum[i - 1], sum[i - 2] + arr[i]), arr[i] + arr[i - 1] + sum[i - 3])

    return sum[n - 1]


# Driver code
arr = [100, 1000, 100, 1000, 1]
n = len(arr)
print
maxSumWO3Consec(arr, n)
