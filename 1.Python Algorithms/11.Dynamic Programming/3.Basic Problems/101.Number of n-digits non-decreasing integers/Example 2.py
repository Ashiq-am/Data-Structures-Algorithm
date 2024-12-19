# Python program To calculate Number of n-digits non-decreasing integers
# Contributed by Parishrut Kushwaha#
# Returns factorial of n
def fact(n):
    res = 1
    for i in range(2, n + 1):
        res = res * i
    return res


# returns nCr
def nCr(n, r):
    return fact(n) // ((fact(r) * fact(n - r)))


# Driver code
n = 2
print("Number of Non-Decreasing digits: ", nCr(n + 9, 9))
