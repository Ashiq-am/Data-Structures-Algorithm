# Python Program to find the length of
# substring with maximum difference of
# zeroes and ones in binary string.
MAX = 100


# Return true if there all 1s
def allones(s, n):
    # Checking each index
    # is 0 or not.
    co = 0

    for i in s:
        co += 1 if i == '1' else 0

    return co == n


# Find the length of substring with
# maximum difference of zeroes and
# ones in binary string
def findlength(arr, s, n, ind, st, dp):
    # If string is over
    if ind >= n:
        return 0

    # If the state is already calculated.
    if dp[ind][st] != -1:
        return dp[ind][st]

    if not st:
        dp[ind][st] = max(arr[ind] +
                          findlength(arr, s, n, ind + 1, 1, dp),
                          (findlength(arr, s, n, ind + 1, 0, dp)))
    else:
        dp[ind][st] = max(arr[ind] +
                          findlength(arr, s, n, ind + 1, 1, dp), 0)

    return dp[ind][st]


# Returns length of substring which is
# having maximum difference of number
# of 0s and number of 1s
def maxLen(s, n):
    # If all 1s return -1.
    if allones(s, n):
        return -1

    # Else find the length.
    arr = [0] * MAX
    for i in range(n):
        arr[i] = 1 if s[i] == '0' else -1

    dp = [[-1] * 3 for _ in range(MAX)]
    return findlength(arr, s, n, 0, 0, dp)


# Driven Program
s = "11000010001"
n = 11
print(maxLen(s, n))
