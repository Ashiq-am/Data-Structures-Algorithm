# Python3 code to find number of days
# after which tank will become empty

# Utility method to get
# sum of first n numbers
def getCumulateSum(n):
    return int((n * (n + 1)) / 2)


# Method returns minimum number of days
# after which tank will become empty
def minDaysToEmpty(C, l):
    # if water filling is more than
    # capacity then after C days only
    # tank will become empty
    if (C <= l): return C

    # initialize binary search variable
    lo, hi = 0, 1e4

    # loop until low is less than high
    while (lo < hi):
        mid = int((lo + hi) / 2)

        # if cumulate sum is greater than (C - l)
        # then search on left side
        if (getCumulateSum(mid) >= (C - l)):
            hi = mid

        # if (C - l) is more then
        # search on right side
        else:
            lo = mid + 1

    # Final answer will be obtained by
    # adding l to binary search result
    return (l + lo)


# Driver code
C, l = 5, 2
print(minDaysToEmpty(C, l))

# This code is contributed by Smitha Dinesh Semwal.
