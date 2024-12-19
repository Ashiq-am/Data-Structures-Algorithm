# Python3 program to calculate
# minimum possible sum for given constraint

# function to calculate min sum using dp
def minSum(ar, n):
    # if elements are less than or equal to 4
    if (n <= 4):
        return min(ar)

    # save start four element as it is
    sum = [0 for i in range(n)]
    sum[0] = ar[0]
    sum[1] = ar[1]
    sum[2] = ar[2]
    sum[3] = ar[3]

    # compute sum[] for all rest elements
    for i in range(4, n):
        sum[i] = ar[i] + min(sum[i - 4:i])

    # Since one of the last 4 elements must be
    # present
    return min(sum[n - 4:n])


# Driver Code
ar = [2, 4, 1, 5, 2, 3, 6, 1, 2, 4]
n = len(ar)
print("Minimum sum = ", minSum(ar, n))
