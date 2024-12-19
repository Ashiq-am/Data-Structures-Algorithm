# Python3 program to choose item with maximum
# sum of weight under given constraint
INT_MIN = -9999999999


def maxWeightRec(wt, val, K, mp, last, diff):
    # memoized recursive method to return maximum
    # weight with K as ratio of weight and values

    # base cases : if no item is remaining
    if last == -1:
        if diff == 0:
            return 0
        else:
            return INT_MIN

    # first make pair with last chosen item and
    # difference between weight and values
    tmp = (last, diff)
    if tmp in mp:
        return mp[tmp]

    # choose maximum value from following two
    # 1) not selecting the current item and
    # calling recursively
    # 2) selection current item, including
    # the weight and updating the difference
    # before calling recursively

    mp[tmp] = max(maxWeightRec(wt, val, K, mp,
                               last - 1, diff), wt[last] +
                  maxWeightRec(wt, val, K, mp,
                               last - 1, diff +
                               wt[last] - val[last] * K))
    return mp[tmp]


def maxWeight(wt, val, K, N):
    # method returns maximum sum of weight with K
    # as ration of sum of weight and their values
    return maxWeightRec(wt, val, K, {}, N - 1, 0)


# Driver code
if __name__ == "__main__":
    wt = [4, 8, 9]
    val = [2, 4, 6]
    N = len(wt)
    K = 2
    print(maxWeight(wt, val, K, N))
