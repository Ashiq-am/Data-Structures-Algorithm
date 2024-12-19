# Python3 program to find if a number
# has alternate bit pattern

# Returns true if n has alternate
# bit pattern else false
def findPattern(n):
    # Store last bit
    prev = n % 2
    n = n // 2

    # Traverse through remaining bits
    while (n > 0):

        curr = n % 2

        # If current bit is same as previous
        if (curr == prev):
            return False

        prev = curr
        n = n // 2

    return True


# Driver code
n = 10
print("Yes") if (findPattern(n)) else print("No")

# This code is contributed by Anant Agarwal.
