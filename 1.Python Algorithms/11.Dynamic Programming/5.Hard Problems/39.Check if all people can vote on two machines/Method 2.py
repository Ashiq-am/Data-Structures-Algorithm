# Python3 program to check if all people can
# vote using two machines within limited
# time

# Returns true if n people can vote using
# two machines in x time.
def canVote(a, n, x):
    # calculate total sum i.e total
    # time taken by all people
    total_sum = 0
    for i in range(len(a)):
        total_sum += a[i]

    # if total time is less than x then
    # all people can definitely vote
    # hence return true
    if (total_sum <= x):
        return True

    # sort the list
    a.sort()

    # declare a list presum of same size
    # as that of a and initialize it with 0
    presum = [0 for i in range(len(a))]

    # prefixsum for first element
    # will be element itself
    presum[0] = a[0]

    # fill the array
    for i in range(1, len(presum)):
        presum[i] = presum[i - 1] + a[i]

    # Set i and j and check if array
    # from i to j - 1 gives sum <= x
    for i in range(0, len(presum)):
        for j in range(i + 1, len(presum)):
            arr1_sum = (presum[i] + (total_sum - presum[j]))
            if ((arr1_sum <= x) and
                    (total_sum - arr1_sum) <= x):
                return True

    return False


# Driver code
n = 3
x = 4
a = [2, 4, 2]
if (canVote(a, n, x)):
    print("YES")
else:
    print("NO")
