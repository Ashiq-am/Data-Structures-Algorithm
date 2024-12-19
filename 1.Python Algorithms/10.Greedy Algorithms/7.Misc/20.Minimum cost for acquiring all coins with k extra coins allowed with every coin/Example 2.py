# Python3 program to acquire all n coins at
# minimum cost with multiple values of k.
import math as mt


# Converts coin[] to prefix sum array
def preprocess(coin, n):
    # sort the coins values
    coin.sort()

    # maintain prefix sum array
    for i in range(1, n):
        coin[i] += coin[i - 1]


# Function to calculate min cost when we can
# get k extra coins after paying cost of one.
def minCost(coin, n, k):
    # calculate no. of coins needed
    coins_needed = mt.ceil(1.0 * n / (k + 1))

    # return sum of from prefix array
    return coin[coins_needed - 1]


# Driver code
coin = [8, 5, 3, 10, 2, 1, 15, 25]

n = len(coin)

preprocess(coin, n)
k = 3

print(minCost(coin, n, k))

k = 7

print(minCost(coin, n, k))
