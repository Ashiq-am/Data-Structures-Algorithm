# Python3 program to find minimum cost to
# get exactly W Kg with given packets
import sys


# Returns the best obtainable price for
# a rod of length n and price[] as prices
# of different pieces
def minCost(cost, n):
    dp = [0 for i in range(n + 1)]

    # Build the table val[] in bottom up
    # manner and return the last entry
    # from the table
    for i in range(1, n + 1):
        min_cost = sys.maxsize

        for j in range(i):
            if j < len(cost) and cost[j] != -1:
                min_cost = min(min_cost,
                               cost[j] + dp[i - j - 1])

        dp[i] = min_cost

    return dp[n]


# Driver code
cost = [10, -1, -1, -1, -1]
W = len(cost)

print(minCost(cost, W))
