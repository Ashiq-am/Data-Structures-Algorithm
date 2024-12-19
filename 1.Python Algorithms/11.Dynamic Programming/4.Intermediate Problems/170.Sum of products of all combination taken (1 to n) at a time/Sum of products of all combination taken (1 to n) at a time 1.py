# Python3 Program to find
# sum of all combination takne
# (1 to N) at a time using
# dynamic programming

# Find the postfix sum array
def postfix(a, n):
    for i in range(n - 1, 1, -1):
        a[i - 1] = a[i - 1] + a[i]


# Modify the array such
# that we don't have to
# compute the products
# which are obtained before
def modify(a, n):
    for i in range(1, n):
        a[i - 1] = i * a[i];


# Finding sum of all combination
# taken 1 to N at a time
def allCombination(a, n):
    sum = 0

    # sum taken 1 at time is
    # simply sum of 1 - N
    for i in range(1, n + 1):
        sum += i
    print("f(1) --> ", sum)

    # for sum of products for
    # all combination
    for i in range(1, n):

        # finding postfix array
        postfix(a, n - i + 1)

        # sum of products taken
        # i+1 at a time
        sum = 0

        for j in range(1, n - i + 1):
            sum += (j * a[j])

        print("f(", i + 1, ") --> ", sum)

        # modify the array for
        # overlapping problem
        modify(a, n)


# Driver's Code
if __name__ == "__main__":

    n = 5
    a = [0] * n

    # storing numbers
    # from 1 to N
    for i in range(n):
        a[i] = i + 1

    # calling allCombination
    allCombination(a, n)
