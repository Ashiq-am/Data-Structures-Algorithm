# Python3 program to find the
# maximum and minimum values
# of an Algebraic expression
# of given form
def minMaxValues(arr, n, m):
    # Finding sum of
    # array elements
    sum = 0
    INF = 1000000000
    MAX = 50
    for i in range(0, (n + m)):
        sum += arr[i]

        # shifting the integers by 50
        # so that they become positive
        arr[i] += 50

    # dp[i][j] represents true
    # if sum j can be reachable
    # by choosing i numbers
    dp = [[0 for x in range(MAX * MAX + 1)]
          for y in range(MAX + 1)]

    dp[0][0] = 1

    # if dp[i][j] is true, that
    # means it is possible to
    # select i numbers from (n + m)
    # numbers to sum upto j
    for i in range(0, (n + m)):

        # k can be at max n because the
        # left expression has n numbers
        for k in range(min(n, i + 1), 0, -1):
            for j in range(0, MAX * MAX + 1):
                if (dp[k - 1][j]):
                    dp[k][j + arr[i]] = 1

    max_value = -1 * INF
    min_value = INF

    for i in range(0, MAX * MAX + 1):

        # checking if a particular
        # sum can be reachable by
        # choosing n numbers
        if (dp[n][i]):
            # getting the actual sum
            # as we shifted the numbers
            # by 50 to avoid negative
            # indexing in array
            temp = i - 50 * n
            max_value = max(max_value,
                            temp * (sum - temp))

            min_value = min(min_value,
                            temp * (sum - temp))

    print("Maximum Value: {}\nMinimum Value: {}"
          .format(max_value, min_value))


# Driver Code
n = 2
m = 2
arr = [1, 2, 3, 4]

minMaxValues(arr, n, m)
