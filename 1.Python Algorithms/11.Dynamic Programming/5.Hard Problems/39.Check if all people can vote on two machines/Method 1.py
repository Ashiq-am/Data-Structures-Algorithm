# Python3 program to check if all people can
# vote using two machines within limited
# time

# Function returns true if n people can vote
# using two machines in x time.
def canVote(a, n, x):
    # dp[i][j] stores maximum possible number
    # of people among arr[0..i-1] can vote
    # in j time.
    dp = [[0] * (x + 1) for _ in range(n + 1)]
    a = a[:]
    a.append(0)

    # Find sum of all times
    sm = 0
    for i in range(n + 1):
        sm += a[i]

    # Fill dp[][] in bottom up manner
    # (Similar to knapsack).
    for i in range(1, n + 1):
        for j in range(1, x + 1):
            if a[i] <= j:
                dp[i][j] = max(dp[i - 1][j], a[i] +
                               dp[i - 1][j - a[i]])
            else:
                dp[i][j] = dp[i - 1][j]

    # If remaining people can go to other machine.
    return (sm - dp[n][x]) <= x


# Driver Code
if __name__ == "__main__":
    n = 3
    x = 4
    a = [2, 4, 2]
    print("YES" if canVote(a, n, x) else "NO")
