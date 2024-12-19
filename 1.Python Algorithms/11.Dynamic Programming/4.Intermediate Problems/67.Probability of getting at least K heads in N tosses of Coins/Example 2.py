# Dynamic and Logarithm approach find probability of
# at least k heads

from math import log2

MAX = 100001

# dp[i] is going to store Log ( i !) in base 2
dp = [0] * MAX


def probability(k, n):
    ans = 0  # Initialize result

    # Iterate from k heads to n heads
    for i in range(k, n + 1):
        res = dp[n] - dp[i] - dp[n - i] - n
        ans = ans + pow(2.0, res)

    return ans


def precompute():
    # Preprocess all the logarithm value on base 2
    for i in range(2, MAX):
        dp[i] = log2(i) + dp[i - 1]


# Driver code
if __name__ == '__main__':
    precompute()

    # Probability of getting 2 head out of 3 coins
    print(probability(2, 3))

    # Probability of getting 3 head out of 6 coins
    print(probability(3, 6))

    # Probability of getting 500 head out of 10000 coins
    print(probability(500, 1000))
