# Python3 Program to calculate
# maximum price of wines
N = 1000
dp = [[-1 for col in range(N)]
      for row in range(N)]

# This array stores the "optimal action"
# for each state i, j
sell = [[0 for col in range(N)]
        for row in range(N)]


# Function to maximize profit
def maxProfitUtil(price, begin, end, n):
    if (dp[begin][end] != -1):
        return dp[begin][end]

    year = n - (end - begin)

    if (begin == end):
        return year * price[begin]

    # x = maximum profit on selling the
    # wine from the front this year
    x = price[begin] * year + \
        maxProfitUtil(price, begin + 1, end, n)

    # y = maximum profit on selling the
    # wine from the end this year
    y = price[end] * year + \
        maxProfitUtil(price, begin, end - 1, n)

    ans = max(x, y)
    dp[begin][end] = ans

    if (x >= y):
        sell[begin][end] = 0
    else:
        sell[begin][end] = 1

    return ans


# Util Function to calculate maxProfit
def maxProfit(price, n):
    ans = maxProfitUtil(price, 0, n - 1, n)

    i = 0
    j = n - 1

    while (i <= j):

        # sell[i][j]=0 implies selling the
        # wine from beginning will be more
        # profitable in the long run
        if (sell[i][j] == 0):
            print("beg", end=" ")
            i = i + 1
        else:
            print("end", end=" ")
            j = j - 1

    print(" ")
    return ans


# Driver code

# Price array
price = [2, 4, 6, 2, 5]

size = 5

ans = maxProfit(price, size)

print(ans)
