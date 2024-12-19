# Python3 program to print maximum
# path sum ending with each position
# x such that all path step positions
# divide x.

def printMaxSum(arr, n):
    # Create an array such that dp[i]
    # stores maximum path sum ending with i.
    dp = [0 for i in range(n)]

    # Calculating maximum sum path
    # for each element.
    for i in range(n):
        dp[i] = arr[i]

        # Finding previous step for arr[i]
        # Moving from 1 to sqrt(i + 1) since all the
        # divisiors are present from sqrt(i + 1).
        maxi = 0
        for j in range(1, int((i + 1) ** 0.5) + 1):

            # Checking if j is divisior of i + 1.
            if ((i + 1) % j == 0 and (i + 1) != j):

                # Checking which divisor will provide
                # greater value.
                if (dp[j - 1] > maxi):
                    maxi = dp[j - 1]
                if (dp[(i + 1) // j - 1] > maxi and j != 1):
                    maxi = dp[(i + 1) // j - 1]

        dp[i] += maxi

    # Printing the answer
    # (Maximum path sum ending
    # with every position i + 1).
    for i in range(n):
        print(dp[i], end=' ')


# Driver Program
arr = [2, 3, 1, 4, 6, 5]
n = len(arr)
printMaxSum(arr, n)


