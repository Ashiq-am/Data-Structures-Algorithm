# Python3 implementation to find minimum
# sum submatrix in a given 2D array
import sys


# Implementation of Kadane's algorithm for
# 1D array. The function returns the minimum
# sum and stores starting and ending indexes
# of the minimum sum subarray at addresses
# pointed by start and finish pointers
# respectively.
def kadane(arr, start, finish, n):
    # Initialize sum, maxSum and
    sum, minSum = 0, sys.maxsize

    # Just some initial value to check
    # for all negative values case
    finish = -1

    # Local variable
    local_start = 0

    for i in range(n):
        sum += arr[i]

        if (sum > 0):
            sum = 0
            local_start = i + 1

        elif (sum < minSum):
            minSum = sum
            start = local_start
            finish = i

    # There is at-least one non-negative number
    if (finish != -1):
        return minSum, start, finish

    # Special Case: When all numbers in arr[]
    # are positive
    minSum = arr[0]
    start, finish = 0, 0

    # Find the minimum element in array
    for i in range(1, n):
        if (arr[i] < minSum):
            minSum = arr[i]
            start = finish = i

    return minSum, start, finish


# Function to find minimum sum submatrix
# in a given 2D array
def findMinSumSubmatrix(M):
    # Variables to store the final output
    minSum = sys.maxsize
    finalLeft = 0
    finalRight = 0
    finalTop = 0
    finalBottom = 0

    # left, right, i = 0, 0, 0
    sum, start, finish = 0, 0, 0

    # Set the left column
    for left in range(5):

        # Initialize all elements of temp as 0
        temp = [0 for i in range(5)]

        # Set the right column for the left
        # column set by outer loop
        for right in range(left, 5):

            # Calculate sum between current left
            # and right for every row 'i'
            for i in range(4):
                temp[i] += M[i][right]

            # Find the minimum sum subarray in temp[].
            # The kadane() function also sets values
            # of start and finish. So 'sum' is sum of
            # rectangle between (start, left) and
            # (finish, right) which is the minimum sum
            # with boundary columns strictly as
            # left and right.
            sum, start, finish = kadane(temp, start,
                                        finish, 4)

            # Compare sum with maximum sum so far. If
            # sum is more, then update maxSum and other
            # output values
            if (sum < minSum):
                minSum = sum
                finalLeft = left
                finalRight = right
                finalTop = start
                finalBottom = finish

    # Print final values
    print("(Top, Left): (", finalTop,
          ",", finalLeft, ")")
    print("(Bottom, Right): (", finalBottom,
          ",", finalRight, ")")
    print("Minimum sum:", minSum)


# Driver code
if __name__ == '__main__':
    M = [[1, 2, -1, -4, -20],
         [-8, -3, 4, 2, 1],
         [3, 8, 10, 1, 3],
         [-4, -1, 1, 7, -6]]

    findMinSumSubmatrix(M)