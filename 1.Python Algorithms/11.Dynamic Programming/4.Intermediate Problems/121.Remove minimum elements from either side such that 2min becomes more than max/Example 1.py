# Python3 implementation of above approach
# A utility function to find
# minimum in arr[l..h]
def mini(arr, l, h):
    mn = arr[l]
    for i in range(l + 1, h + 1):
        if (mn > arr[i]):
            mn = arr[i]
    return mn


# A utility function to find
# maximum in arr[l..h]
def max(arr, l, h):
    mx = arr[l]
    for i in range(l + 1, h + 1):
        if (mx < arr[i]):
            mx = arr[i]
    return mx


# Returns the minimum number of
# removals from either end in
# arr[l..h] so that 2*min becomes
# greater than max.
def minRemovals(arr, l, h):
    # If there is 1 or less elements, return 0
    # For a single element, 2*min > max
    # (Assumption: All elements are positive in arr[])
    if (l >= h):
        return 0

    # 1) Find minimum and maximum
    # in arr[l..h]
    mn = mini(arr, l, h)
    mx = max(arr, l, h)

    # If the property is followed,
    # no removals needed
    if (2 * mn > mx):
        return 0

    # Otherwise remove a character from
    # left end and recur, then remove a
    # character from right end and recur,
    # take the minimum of two is returned
    return (min(minRemovals(arr, l + 1, h),
                minRemovals(arr, l, h - 1)) + 1)


# Driver Code
arr = [4, 5, 100, 9, 10,
       11, 12, 15, 200]
n = len(arr)
print(minRemovals(arr, 0, n - 1))
