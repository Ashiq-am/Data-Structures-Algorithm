# Python3 program to find the maximum
# sum such that no three are consecutive
# using recursion.
arr = [100, 1000, 100, 1000, 1]
sum = [-1] * 10000


# Returns maximum subsequence sum such
# that no three elements are consecutive
def maxSumWO3Consec(n):
    if (sum[n] != -1):
        return sum[n]

    # 3 Base cases (process first
    # three elements)
    if (n == 0):
        sum[n] = 0
        return sum[n]

    if (n == 1):
        sum[n] = arr[0]
        return sum[n]

    if (n == 2):
        sum[n] = arr[1] + arr[0]
        return sum[n]

    # Process rest of the elements
    # We have three cases
    sum[n] = max(max(maxSumWO3Consec(n - 1),
                     maxSumWO3Consec(n - 2) + arr[n]),
                 arr[n] + arr[n - 1] +
                 maxSumWO3Consec(n - 3))

    return sum[n]


# Driver code
if __name__ == "__main__":
    n = len(arr)

    print(maxSumWO3Consec(n))
