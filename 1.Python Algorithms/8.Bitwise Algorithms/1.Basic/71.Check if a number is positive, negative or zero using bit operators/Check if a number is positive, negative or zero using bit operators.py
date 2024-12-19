# Python 3 program to
# find if a number is
# positive, negative
# or zero using
# bit wise operators.

# function to return 1 if it is zero
# returns 0 if it is negative
# returns 2 if it is positive
def index(i):
    return 1 + (i >> 31) - (-i >> 31)


def check(n):
    # string array to store all kinds of number
    s = "negative", "zero", "positive"

    # function call to check the sign of number
    val = index(n)

    print(n, "is", s[val])


# driver program to
# test the above function
check(30)
check(-20)
check(0)

# This code is contributed by
# Smitha Dinesh Semwal
