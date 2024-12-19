# Python3 program to calculate the number of
# n digit stepping numbers.

# function that calculates the answer
def answer(n):
    # dp[j] stores count of i digit
    # stepping numbers ending with digit j.
    dp = [0] * 10

    # To store resu1lt of length i - 1
    # before updating dp[j] for length i.
    prev = [0] * 10

    # if n is 1 then answer will be 10.
    if (n == 1):
        return 10

    # Initialize values for count of
    # digits equal to 1.
    for j in range(0, 10):
        dp[j] = 1

    # Compute values for count of digits
    # more than 1.
    for i in range(2, n + 1):
        for j in range(0, 10):
            prev[j] = dp[j]

        for j in range(0, 10):

            # If ending digit is 0
            if (j == 0):
                dp[j] = prev[j + 1]

            # If ending digit is 9
            elif (j == 9):
                dp[j] = prev[j - 1]

            # For other digits.
            else:
                dp[j] = prev[j - 1] + prev[j + 1]

    # stores the final answer
    sum = 0
    for j in range(1, 10):
        sum = sum + dp[j]
    return sum


# Driver Code
n = 2
print(answer(n))
