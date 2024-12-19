# Python 3 program to calculate all
# triplets whose sum is perfect cube.

dp = [[0 for i in range(15001)]
      for j in range(1001)]


# Function to calculate all occurrence
# of a number in a given range
def computeDpArray(arr, n):
    for i in range(n):
        for j in range(1, 15001, 1):

            # if i == 0
            # assign 1 to present state
            if (i == 0):
                dp[i][j] = (j == arr[i])

            # else add +1 to current state with
            # previous state
            else:
                dp[i][j] = dp[i - 1][j] + (arr[i] == j)


# Function to calculate triplets whose
# sum is equal to the perfect cube
def countTripletSum(arr, n):
    computeDpArray(arr, n)

    ans = 0  # Initialize answer
    for i in range(0, n - 2, 1):
        for j in range(i + 1, n - 1, 1):
            for k in range(1, 25, 1):
                cube = k * k * k

                rem = cube - (arr[i] + arr[j])

                # count all occurrence of third
                # triplet in range from j+1 to n
                if (rem > 0):
                    ans += dp[n - 1][rem] - dp[j][rem]

    return ans


# Driver code
if __name__ == '__main__':
    arr = [2, 5, 1, 20, 6]
    n = len(arr)
    print(countTripletSum(arr, n))
