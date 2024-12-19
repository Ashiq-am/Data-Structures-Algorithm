# Python3 program to find out maximum
# profit by buying and/ selling a share
# at most k times given the stock price
# of n days

# Function to find out maximum profit
# by buying & selling/ a share atmost
# k times given stock price of n days
def maxProfit(price, n, k):
    # Table to store results of subproblems
    # profit[t][i] stores maximum profit
    # using atmost t transactions up to
    # day i (including day i)
    profit = [[0 for i in range(n + 1)]
              for j in range(k + 1)]

    # Fill the table in bottom-up fashion
    for i in range(1, k + 1):
        prevDiff = float('-inf')

        for j in range(1, n):
            prevDiff = max(prevDiff,
                           profit[i - 1][j - 1] -
                           price[j - 1])
            profit[i][j] = max(profit[i][j - 1],
                               price[j] + prevDiff)

    return profit[k][n - 1]


# Driver Code
if __name__ == "__main__":
    k = 3
    price = [12, 14, 17, 10, 14, 13, 12, 15]
    n = len(price)

    print("Maximum profit is:",
          maxProfit(price, n, k))