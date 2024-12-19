# Python3 code to maximize result when
# we have choice to divide or consider
# as it is.

# function for calculating max
# possible result
def maxDP(n):
    res = list()
    res.append(0)
    res.append(1)

    # Compute remaining values in
    # bottom up manner.
    i = 2
    while i < n + 1:
        res.append(max(i, (res[int(i / 2)] + res[int(i / 3)] + res[int(i / 4)]
                           + res[int(i / 5)])))
        i = i + 1

    return res[n]


# driver code
n = 60
print("MaxSum =", maxDP(n))
