# Python3 Program to find first
# n terms of Golomb sequence.

# Print the first n term
# of Golomb Sequence
def Golomb(n):
    dp = [0] * (n + 1)

    # base cases
    dp[1] = 1
    print(dp[1], end=" ")

    # Finding and pring first
    # n terms of Golomb Sequence.
    for i in range(2, n + 1):
        dp[i] = 1 + dp[i - dp[dp[i - 1]]]
        print(dp[i], end=" ")


# Driver Code
n = 9

Golomb(n)
