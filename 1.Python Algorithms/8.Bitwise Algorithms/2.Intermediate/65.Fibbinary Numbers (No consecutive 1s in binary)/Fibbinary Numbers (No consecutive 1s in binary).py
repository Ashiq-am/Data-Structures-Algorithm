# Python 3 program to check if a
# number is fibinnary number or
# not

# function to check if binary
# representation of an integer
# has consecutive 1s
def checkFibinnary(n):
    # stores the previous last bit
    # initially as 0
    prev_last = 0

    while (n):

        # if current last bit and
        # previous last bit is 1
        if ((n & 1) and prev_last):
            return False

        # stores the last bit
        prev_last = n & 1

        # right shift the number
        n >>= 1

    return True


# Driver code
n = 10

if (checkFibinnary(n)):
    print("YES")
else:
    print("NO")

# This code is contributed by Smitha Dinesh Semwal
