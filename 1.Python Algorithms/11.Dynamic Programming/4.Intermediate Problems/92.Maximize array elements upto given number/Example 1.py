# Python3 code to find maximum
# value of number obtained by
# using array elements recursively.

# Utility def to find
# maximum possible value

# variable to store maximum value
# that can be obtained.
ans = 0


def findMaxValUtil(arr, n, num, maxLimit, ind):
    global ans

    # If entire array is traversed,
    # then compare current value
    # in num to overall maximum
    # obtained so far.
    if (ind == n):
        ans = max(ans, num)
        return

    # Case 1: Subtract current element
    # from value so far if result is
    # greater than or equal to zero.
    if (num - arr[ind] >= 0):
        findMaxValUtil(arr, n, num - arr[ind],
                       maxLimit, ind + 1)

    # Case 2 : Add current element to
    # value so far if result is less
    # than or equal to maxLimit.
    if (num + arr[ind] <= maxLimit):
        findMaxValUtil(arr, n, num + arr[ind],
                       maxLimit, ind + 1)


# def to find maximum possible
# value that can be obtained using
# array elements and given number.
def findMaxVal(arr, n, num, maxLimit):
    global ans
    # variable to store
    # current index position.
    ind = 0

    # call to utility def to
    # find maximum possible value
    # that can be obtained.
    findMaxValUtil(arr, n, num, maxLimit, ind)
    return ans


# Driver code
num = 1
arr = [3, 10, 6, 4, 5]
n = len(arr)
maxLimit = 15

print(findMaxVal(arr, n, num, maxLimit))


