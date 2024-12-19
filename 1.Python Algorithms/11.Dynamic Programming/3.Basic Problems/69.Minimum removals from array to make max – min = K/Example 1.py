# Python program to find
# minimum removals to
# make max-min <= K
MAX = 100
dp = [[0 for i in range(MAX)]
      for i in range(MAX)]
for i in range(0, MAX):
    for j in range(0, MAX):
        dp[i][j] = -1


# function to check all
# possible combinations
# of removal and return
# the minimum one
def countRemovals(a, i, j, k):
    global dp

    # base case when all
    # elements are removed
    if (i >= j):
        return 0

    # if condition is satisfied,
    # no more removals are required
    elif ((a[j] - a[i]) <= k):
        return 0

    # if the state has
    # already been visited
    elif (dp[i][j] != -1):
        return dp[i][j]

    # when Amax-Amin>d
    elif ((a[j] - a[i]) > k):

        # minimum is taken of
        # the removal of minimum
        # element or removal of
        # the maximum element
        dp[i][j] = 1 + min(countRemovals(a, i + 1,
                                         j, k),
                           countRemovals(a, i,
                                         j - 1, k))
    return dp[i][j]


# To sort the array
# and return the answer
def removals(a, n, k):
    # sort the array
    a.sort()

    # fill all stated
    # with -1 when only
    # one element
    if (n == 1):
        return 0
    else:
        return countRemovals(a, 0,
                             n - 1, k)


# Driver Code
a = [1, 3, 4, 9, 10,
     11, 12, 17, 20]
n = len(a)
k = 4
print(removals(a, n, k))
