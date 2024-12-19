# Python Program to find 2 Missing
# Numbers using O(1) extra space

# Returns the sum of the array
def getSum(arr, n):
    sum = 0;
    for i in range(0, n):
        sum += arr[i]
    return sum


# Function to find two missing
# numbers in range [1, n]. This
# function assumes that size of
# array is n-2 and all array
# elements are distinct
def findTwoMissingNumbers(arr, n):
    # Sum of 2 Missing Numbers
    sum = ((n * (n + 1)) / 2 -
           getSum(arr, n - 2));

    # Find average of two elements
    avg = (sum / 2);

    # Find sum of elements smaller
    # than average (avg) and sum
    # of elements greater than
    # average (avg)
    sumSmallerHalf = 0
    sumGreaterHalf = 0;
    for i in range(0, n - 2):

        if (arr[i] <= avg):
            sumSmallerHalf += arr[i]
        else:
            sumGreaterHalf += arr[i]

    print("Two Missing Numbers are")

    # The first (smaller) element = (sum
    # of natural numbers upto avg) - (sum
    # of array elements smaller than or
    # equal to avg)
    totalSmallerHalf = (avg * (avg + 1)) / 2
    print(str(totalSmallerHalf -
              sumSmallerHalf) + " ")

    # The first (smaller) element = (sum
    # of natural numbers from avg+1 to n) -
    # (sum of array elements greater than avg)
    print(str(((n * (n + 1)) / 2 -
               totalSmallerHalf) -
              sumGreaterHalf))


# Driver Code
arr = [1, 3, 5, 6]

# Range of numbers is 2
# plus size of array
n = 2 + len(arr)

findTwoMissingNumbers(arr, n)

# This code is contributed
# by Yatin Gupta
