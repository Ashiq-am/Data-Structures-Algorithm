# Python 3 program to find position
# of only set bit in a given number

# A utility function to check whether
# n is power of 2 or not
def isPowerOfTwo(n):
    return (n and (not (n & (n - 1))))


# Returns position of the only set bit in 'n'
def findPosition(n):
    if not isPowerOfTwo(n):
        return -1

    count = 0

    # One by one move the only set bit to
    # right till it reaches end
    while (n):
        n = n >> 1

        # increment count of shifts
        count += 1

    return count


# Driver program to test above function
if __name__ == "__main__":
    n = 0
    pos = findPosition(n)

    if pos == -1:
        print("n =", n, "Invalid number")
    else:
        print("n =", n, "Position", pos)

    n = 12
    pos = findPosition(n)

    if pos == -1:
        print("n =", n, "Invalid number")
    else:
        print("n =", n, "Position", pos)

    n = 128
    pos = findPosition(n)

    if pos == -1:
        print("n =", n, "Invalid number")
    else:
        print("n =", n, "Position", pos)

# This code is contributed by ANKITRAI1
