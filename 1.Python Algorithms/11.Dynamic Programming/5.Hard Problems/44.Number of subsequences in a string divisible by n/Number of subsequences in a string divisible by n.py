# Python 3 program to count subsequences
# of a string divisible by n.

# Returns count of subsequences of
# str divisible by n.
def countDivisibleSubseq(str, n):
    l = len(str)

    # division by n can leave only n remainder
    # [0..n-1]. dp[i][j] indicates number of
    # subsequences in string [0..i] which leaves
    # remainder j after division by n.
    dp = [[0 for x in range(l)]
          for y in range(n)]

    # Filling value for first digit in str
    dp[int(str[0]) % n][0] += 1

    for i in range(1, l):

        # start a new subsequence with index i
        dp[int(str[i]) % n][i] += 1

        for j in range(n):
            # exclude i'th character from all the
            # current subsequences of string [0...i-1]
            dp[j][i] += dp[j][i - 1]

            # include i'th character in all the current
            # subsequences of string [0...i-1]
            dp[(j * 10 + int(str[i])) % n][i] += dp[j][i - 1]

    return dp[0][l - 1]


# Driver code
if __name__ == "__main__":
    str = "1234"
    n = 4
    print(countDivisibleSubseq(str, n))

# This code is contributed by ita_c
