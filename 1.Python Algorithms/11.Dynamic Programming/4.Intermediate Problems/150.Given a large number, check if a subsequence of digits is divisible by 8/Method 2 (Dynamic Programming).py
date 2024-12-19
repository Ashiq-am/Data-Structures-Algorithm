# Python3 program to find
# if there is a subsequence
# of digits divisible by 8.

# Function takes in an array of numbers,
# dynamically goes on the location and
# makes combination of numbers.
def isSubSeqDivisible(str):
    n = len(str)
    dp = [[0 for i in range(10)]
          for i in range(n + 1)]

    # Converting string to integer
    # array for ease of computations
    # (Indexing in arr[] is considered
    # to be starting from 1)
    arr = [0 for i in range(n + 1)]
    for i in range(1, n + 1):
        arr[i] = int(str[i - 1])

    for i in range(1, n + 1):
        dp[i][arr[i] % 8] = 1
        for j in range(8):

            # If we consider the number
            # in our combination, we add
            # it to the previous combination
            if (dp[i - 1][j] > dp[i][(j * 10 + arr[i]) % 8]):
                dp[i][(j * 10 + arr[i]) % 8] = dp[i - 1][j]

            # If we exclude the number
            # from our combination
            if (dp[i - 1][j] > dp[i][j]):
                dp[i][j] = dp[i - 1][j]

    for i in range(1, n + 1):

        # If at dp[i][0], we find
        # value 1/true, it shows
        # that the number exists
        # at the value of 'i'
        if (dp[i][0] == 1):
            return True
    return False


# Driver Code
str = "3144"
if (isSubSeqDivisible(str)):
    print("Yes")
else:
    print("No")
