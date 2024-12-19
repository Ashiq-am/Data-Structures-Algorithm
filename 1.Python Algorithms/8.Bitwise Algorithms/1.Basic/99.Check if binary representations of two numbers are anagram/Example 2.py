# Python3 program to check if binary
# representations of two numbers are anagrams.

# Check each bit in a number is set or not
# and return the total count of the set bits.
def countSetBits(n):
    count = 0
    while n > 0:
        count += n & 1
        n >>= 1
    return count


def areAnagrams(A, B):
    return countSetBits(A) == countSetBits(B)


# Driver code
if __name__ == "__main__":

    a, b = 8, 4
    if areAnagrams(a, b):
        print("1")
    else:
        print("0")

# this code is contributed by aditya942003patil
