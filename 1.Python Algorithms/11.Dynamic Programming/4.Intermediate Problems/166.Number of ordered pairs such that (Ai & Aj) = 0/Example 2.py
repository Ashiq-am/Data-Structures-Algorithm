# Python program to calculate the number
# of ordered pairs such that their bitwise
# and is zero
N = 15


# efficient function to count pairs
def countPairs(a, n):
    # stores the frequency of each number
    Hash = {}

    # initialize 0 to all
    dp = [[0 for i in range(N + 1)] for j in range(1 << N)]

    # count the frequency of every element
    for i in range(n):
        if a[i] not in Hash:
            Hash[a[i]] = 1
        else:
            Hash[a[i]] += 1

    # iterate for al possible values that a[i] can be
    mask = 0
    while (mask < (1 << N)):
        if mask not in Hash:
            Hash[mask] = 0

        # if the last bit is ON
        if (mask & 1):
            dp[mask][0] = Hash[mask] + Hash[mask ^ 1]

        else:  # is the last bit is OFF
            dp[mask][0] = Hash[mask]

        # iterate till n
        for i in range(1, N + 1):

            # if mask's ith bit is set
            if (mask & (1 << i)):
                dp[mask][i] = dp[mask][i - 1] + dp[mask ^ (1 << i)][i - 1]

            else:  # if mask's ith bit is not set
                dp[mask][i] = dp[mask][i - 1]

        mask += 1

    ans = 0

    # iterate for all the array element
    # and count the number of pairs
    for i in range(n):
        ans += dp[((1 << N) - 1) ^ a[i]][N]

    # return answer
    return ans


# Driver Code
a = [5, 4, 1, 6]
n = len(a)
print(countPairs(a, n))
