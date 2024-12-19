# Python3 program to find maximum elements
# that can be made equal with k updates

# Function to calculate the maximum number of
# equal elements possible with atmost K increment
# of values .Here we have done sliding window
# to determine that whether there are x number of
# elements present which on increment will become
# equal. The loop here will run in fashion like
# 0...x-1, 1...x, 2...x+1, ...., n-x-1...n-1
def ElementsCalculationFunc(pre, maxx,
                            x, k, n):
    i = 0
    j = x
    while j <= n:

        # It can be explained with the reasoning
        # that if for some x number of elements
        # we can update the values then the
        # increment to the segment (i to j having
        # length -> x) so that all will be equal is
        # (x*maxx[j]) this is the total sum of
        # segment and (pre[j]-pre[i]) is present sum
        # So difference of them should be less than k
        # if yes, then that segment length(x) can be
        # possible return true
        if (x * maxx[j] - (pre[j] - pre[i]) <= k):
            return True

        i += 1
        j += 1

    return False


def MaxNumberOfElements(a, n, k):
    # sort the array in ascending order
    a.sort()
    pre = [0] * (n + 1)  # prefix sum array
    maxx = [0] * (n + 1)  # maximum value array

    # Initializing the prefix array
    # and maximum array
    for i in range(n + 1):
        pre[i] = 0
        maxx[i] = 0

    for i in range(1, n + 1):
        # Calculating prefix sum of the array
        pre[i] = pre[i - 1] + a[i - 1]

        # Calculating max value upto that
        # position in the array
        maxx[i] = max(maxx[i - 1], a[i - 1])

    # Binary search applied for
    # computation here
    l = 1
    r = n
    while (l < r):
        mid = (l + r) // 2

        if (ElementsCalculationFunc(pre, maxx,
                                    mid - 1, k, n)):
            ans = mid
            l = mid + 1

        else:
            r = mid - 1

    # printing result
    print(ans)


# Driver Code
if __name__ == "__main__":
    arr = [2, 4, 9]
    n = len(arr)
    k = 3
    MaxNumberOfElements(arr, n, k)
