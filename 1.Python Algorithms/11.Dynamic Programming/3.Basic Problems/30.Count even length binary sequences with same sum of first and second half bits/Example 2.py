# A memoization based python program to count even
# length binary sequences such that the sum of
# first and second half bits is same

MAX = 1000

# A lookup table to store the results of subproblems
lookup = [[0 for i in range(MAX)] for i in range(MAX)]


# dif is difference between sums of first n bits
# and last n bits i.e., dif = (Sum of first n bits) -
#							 (Sum of last n bits)
def countSeqUtil(n, dif):
    # We can't cover difference of more
    # than n with 2n bits
    if abs(dif) > n:
        return 0
    # n == 1, i.e., 2 bit long sequences
    if n == 1 and dif == 0:
        return 2
    if n == 1 and abs(dif) == 1:
        return 1

    # Check if this subproblem is already solved
    # n is added to dif to make sure index becomes
    # positive
    if lookup[n][n + dif] != -1:
        return lookup[n][n + dif]

    # First bit is 0 & last bit is 1
    # +First and last bits are same
    # +First bit is 1 & last bit is 0
    res = (countSeqUtil(n - 1, dif + 1) +
           2 * countSeqUtil(n - 1, dif) +
           countSeqUtil(n - 1, dif - 1))

    # Store result in lookup table and return the result
    lookup[n][n + dif] = res
    return res


# A Wrapper over countSeqUtil(). It mainly initializes lookup
# table, then calls countSeqUtil()
def countSeq(n):
    # Initialize all entries of lookup table as not filled
    global lookup
    lookup = [[-1 for i in range(MAX)] for i in range(MAX)]
    # call countSeqUtil()
    res = countSeqUtil(n, 0)
    return res


# Driver Code
if __name__ == '__main__':
    n = 2
    print('Count of Sequences is ', countSeq(n))
