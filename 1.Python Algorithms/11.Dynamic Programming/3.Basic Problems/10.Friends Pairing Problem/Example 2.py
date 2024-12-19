# Python3 program for solution of friends
# pairing problem Using Recursion
dp = [-1] * 1000


# Returns count of ways n people
# can remain single or paired up.
def countFriendsPairings(n):
    global dp

    if (dp[n] != -1):
        return dp[n]

    if (n > 2):

        dp[n] = (countFriendsPairings(n - 1) +
                 (n - 1) * countFriendsPairings(n - 2))
        return dp[n]

    else:
        dp[n] = n
        return dp[n]


# Driver Code
n = 4
print(countFriendsPairings(n))
