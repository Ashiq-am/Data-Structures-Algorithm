# Python3 code to find count of arrays.

# Return the number of lists with
# given constraints.
def countarray(n, k, x):
    dp = list()

    # Initialising dp[0] and dp[1]
    dp.append(0)
    dp.append(1)

    # Computing f(i) for each 2 <= i <= n.
    i = 2
    while i < n:
        dp.append((k - 2) * dp[i - 1] +
                  (k - 1) * dp[i - 2])
        i = i + 1

    return ((k - 1) * dp[n - 2] if x == 1 else dp[n - 1])


# Driven code
n = 4
k = 3
x = 2
print(countarray(n, k, x))
