# Python3 program to find solution of
# Josephus problem when size of step is 2.

# Returns position of survivor among a
# circle of n persons and every second
# person being killed
def josephus(n):
    # Find value of 2 ^ (1 + floor(Log n))
    # which is a power of 2 whose value
    # is just above n.
    p = 1
    while p <= n:
        p *= 2

    # Return 2n - 2^(1 + floor(Logn)) + 1
    return (2 * n) - p + 1


# Driver Code
n = 16
print("The chosen place is", josephus(n))

# This code is contributed by Shreyanshi Arun.
