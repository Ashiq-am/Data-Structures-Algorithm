# Python code to find the count of
# odd numbers in n-th row of
# Pascal's Triangle

# Function to get no of set
# bits in binary representation
# of positive integer n
def countSetBits(n):
    count = 0
    while n:
        count += n & 1
        n >>= 1

    return count


def countOfOddPascal(n):
    # Count number of 1's in binary
    # representation of n.
    c = countSetBits(n)

    # Number of odd numbers in n-th
    # row is 2 raised to power the count.
    return pow(2, c)


# Driver Program
n = 20
print(countOfOddPascal(n))

# This code is contributed by Shrikant13
