# A Naive Recursive Python
# program to count even length
# binary sequences such that
# the sum of first and second
# half bits is same

# diff is difference between
# sums first n bits and last
# n bits respectively
def countSeq(n, diff):
    # We can't cover difference
    # of more than n with 2n bits
    if (abs(diff) > n):
        return 0

    # n == 1, i.e., 2
    # bit long sequences
    if (n == 1 and diff == 0):
        return 2
    if (n == 1 and abs(diff) == 1):
        return 1

    # First bit is 0 & last bit is 1
    # First and last bits are same
    # First bit is 1 & last bit is 0
    res = (countSeq(n - 1, diff + 1) +
           2 * countSeq(n - 1, diff) +
           countSeq(n - 1, diff - 1))

    return res


# Driver Code
n = 2
print("Count of sequences is %d " %
      (countSeq(2, 0)))


