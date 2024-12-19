# A DP based solution to find
# Jacobsthal and Jacobsthal-
# Lucas numbers

# Return nth Jacobsthal number.
def Jacobsthal(n):
    dp = [0] * (n + 1)

    # base case
    dp[0] = 0
    dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + 2 * dp[i - 2]

    return dp[n]


# Return nth Jacobsthal-
# Lucas number.
def Jacobsthal_Lucas(n):
    dp = [0] * (n + 1)

    # base case
    dp[0] = 2
    dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + 2 * dp[i - 2]

    return dp[n]


# Driven Program
n = 5

print("Jacobsthal number:", Jacobsthal(n))
print("Jacobsthal-Lucas number:", Jacobsthal_Lucas(n))

