# Python code for the above approach
from math import ceil, sqrt


def swapNibbles(N):
    # Step 1
    right = (N & 0b00001111)

    # Step 3
    right = (right << 4)

    # Step 2
    left = (N & 0b11110000)

    # Step 4
    left = (left >> 4)

    # Step 5
    return (right | left)


# Driver Code
n = 100;
print("Original: ", n, end=" ")
print(" Swapped: ", swapNibbles(n))

# This code is contributed by code_hunt.
