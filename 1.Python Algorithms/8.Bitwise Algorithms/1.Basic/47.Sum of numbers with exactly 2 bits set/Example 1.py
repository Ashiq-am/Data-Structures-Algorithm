# Python program to find
# sum of numbers
# upto n whose 2 bits are set

# To count number of set bits
def countSetBits(n):
    count = 0
    while (n):
        n = n & (n - 1)
        count = count + 1

    return count


# To calculate sum of numbers
def findSum(n):
    sum = 0

    # To count sum of number
    # whose 2 bit are set
    for i in range(1, n + 1):
        if (countSetBits(i) == 2):
            sum = sum + i

    return sum


# Driver code
n = 10
print(findSum(n))

# This code is contributed
# by Anant Agarwal.
