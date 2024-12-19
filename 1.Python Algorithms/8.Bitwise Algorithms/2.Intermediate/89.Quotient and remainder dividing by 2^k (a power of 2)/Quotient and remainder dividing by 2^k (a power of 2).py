# Python 3 to find remainder and
# quotient
import math


# function to print remainder and
# quotient
def divide(n, m):
    # print Remainder by
    # n AND (m-1)
    print("Remainder = ",
          ((n) & (m - 1)))

    # print quotient by
    # right shifting n by
    # (log2(m)) times
    print("Quotient = ", (n >>
                          (int)(math.log2(m))))


# driver program
n = 43
m = 8
divide(n, m)

# This code is contributed by
# Smitha
