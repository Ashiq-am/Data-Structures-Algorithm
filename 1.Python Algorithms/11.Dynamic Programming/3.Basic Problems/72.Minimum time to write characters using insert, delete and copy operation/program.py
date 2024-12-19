# Python3 program to write characters in
# minimum time by inserting, removing
# and copying operation

def minTimeForWritingChars(N, insert,
                           remov, cpy):
    # method returns minimum time
    # to write 'N' characters
    if N == 0:
        return 0
    if N == 1:
        return insert

    # declare dp array and initialize
    # with zero
    dp = [0] * (N + 1)

    # first char will always take insertion time
    dp[1] = insert

    # loop for 'N' number of times
    for i in range(2, N + 1):

        # if current char count is even then
        # choose minimum from result for (i-1)
        # chars and time for insertion and
        # result for half of chars and time
        # for copy
        if i % 2 == 0:
            dp[i] = min(dp[i - 1] + insert,
                        dp[i // 2] + cpy)

        # if current char count is odd then
        # choose minimum from
        # result for (i-1) chars and time for
        # insertion and
        # result for half of chars and time for
        # copy and one extra character deletion
        else:
            dp[i] = min(dp[i - 1] + insert,
                        dp[(i + 1) // 2] +
                        cpy + remov)

    return dp[N]


# Driver Code
if __name__ == "__main__":
    N = 9
    insert = 1
    remov = 2
    cpy = 1
    print(minTimeForWritingChars(N, insert,remov, cpy))
