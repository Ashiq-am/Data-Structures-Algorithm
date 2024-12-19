# Python3 Program to find
# Newman–Shanks–Williams prime

# return nth Newman–Shanks
# –Williams prime
def nswp(n):
    # Base case
    dp = [1 for x in range(n + 1)]

    # Finding nth Newman–Shanks
    # –Williams prime
    for i in range(2, n + 1):
        dp[i] = (2 * dp[i - 1] +
                 dp[i - 2])
    return dp[n]


# Driver Code
n = 3
print(nswp(n))

