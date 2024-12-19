# A simple Python 3 program
# to check for even or odd

# Returns true if n
# is even, else odd
def isEven(n):
    # Return true if
    # n/2 does not result
    # in a float value.
    return (int(n / 2) * 2 == n)


# Driver code
n = 101
if (isEven(n) != False):
    print("Even")
else:
    print("Odd")

# This code is contributed by
# Smitha Dinesh Semwal.
