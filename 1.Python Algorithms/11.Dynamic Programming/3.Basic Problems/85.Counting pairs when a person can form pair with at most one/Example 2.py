# Python program to find Number of ways
# in which participant can take part.

# Function to calculate number of ways.
def numberOfWays(x):
    dp = []
    dp.append(1)
    dp.append(1)
    for i in range(2, x + 1):
        dp.append(dp[i - 1] + (i - 1) * dp[i - 2])
    return (dp[x])


# Driver code
x = 3
print(numberOfWays(x))
