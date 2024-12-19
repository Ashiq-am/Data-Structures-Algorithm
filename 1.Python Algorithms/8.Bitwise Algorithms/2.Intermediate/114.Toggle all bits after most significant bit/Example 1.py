# Python program to toggle
# set bits starting
# from MSB

def toggle(n):
    # temporary variable to
    # use XOR with one of a n
    temp = 1

    # Run loop until the only
    # set bit in temp crosses
    # MST of n.
    while (temp <= n):
        # Toggle bit of n
        # corresponding to
        # current set bit in
        # temp.
        n = n ^ temp

        # Move set bit to next
        # higher position.
        temp = temp << 1

    return n


# Driver code

n = 10
n = toggle(n)
print(n)

# This code is contributed
# by Anant Agarwal.
