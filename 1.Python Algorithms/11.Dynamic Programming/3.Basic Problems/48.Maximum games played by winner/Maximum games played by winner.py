# Python3 program to find maximum
# number of games played by winner

# method returns maximum games
# a winner needs to play in
# N-player tournament

def maxGameByWinner(N):
    dp = [0 for i in range(N)]

    # for 0 games, 1 player is needed
    # for 1 game, 2 players are required
    dp[0] = 1
    dp[1] = 2

    # loop until i-th Fibonacci
    # number is less than or
    # equal to N
    i = 1
    while dp[i] <= N:
        i = i + 1
        dp[i] = dp[i - 1] + dp[i - 2]

    # result is (i - 1) because i will be
    # incremented one extra in while loop
    # and we want the last value which is
    # smaller than N, so
    return (i - 1)


# Driver code
N = 10
print(maxGameByWinner(N))

# This code is contributed
# by sahilshelangia
