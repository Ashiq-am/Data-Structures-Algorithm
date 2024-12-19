# Python3 program to find maximum
# value of number obtained by
# using array elements by using
# dynamic programming.


# Function to find maximum
# possible value of number
# that can be obtained
# using array elements.
def findMaxVal(arr, n, num, maxLimit):
    # Variable to represent
    # current index.
    ind = -1

    # Variable to show value
    # between 0 and maxLimit.
    val = -1

    # Table to store whether
    # a value can be obtained
    # or not upto a certain
    # index 1. dp[i,j] = 1 if
    # value j can be obtained
    # upto index i.
    # 2. dp[i,j] = 0 if value j
    # cannot be obtained upto index i.
    dp = [[0 for i in range(maxLimit + 1)] for j in range(n)]

    for ind in range(n):
        for val in range(maxLimit + 1):

            # Check for index 0 if given
            # value val can be obtained
            # by either adding to or
            # subtracting arr[0] from num.
            if (ind == 0):
                if (num - arr[ind] == val or num + arr[ind] == val):
                    dp[ind][val] = 1
                else:
                    dp[ind][val] = 0

            else:

                # 1. If arr[ind] is added
                # to obtain given val then
                # val- arr[ind] should be
                # obtainable from index
                # ind-1.
                # 2. If arr[ind] is subtracted
                # to obtain given val then
                # val+arr[ind] should be
                # obtainable from index ind-1.
                # Check for both the conditions.
                if (val - arr[ind] >= 0 and val + arr[ind] <= maxLimit):

                    # If either of one condition
                    # is True, then val is
                    # obtainable at index ind.
                    if (dp[ind - 1][val - arr[ind]] == 1 or
                            dp[ind - 1][val + arr[ind]] == 1):
                        dp[ind][val] = 1

                elif (val - arr[ind] >= 0):
                    dp[ind][val] = dp[ind - 1][val - arr[ind]]
                elif (val + arr[ind] <= maxLimit):
                    dp[ind][val] = dp[ind - 1][val + arr[ind]]
                else:
                    dp[ind][val] = 0

    # Find maximum value that
    # is obtained at index n-1.
    for val in range(maxLimit, -1, -1):
        if (dp[n - 1][val] == 1):
            return val

    # If no solution
    # exists return -1.
    return -1


# Driver Code
if __name__ == '__main__':
    num = 1
    arr = [3, 10, 6, 4, 5]
    n = len(arr)
    maxLimit = 15

    print(findMaxVal(arr, n, num, maxLimit))


