# Python program to print
# first n pernicious numbers

# function to check
# prime number
def isPrime(x):
    if x < 2:
        return False

    for i in range(2, x):
        if not x % i:
            return False

    return True


# Prints first n Pernicious
# numbers
def printPernicious(n):
    i, count = 1, 0

    while count < n:

        # "bin(i).count('1')" count
        # no of ones in binary
        # representation
        if (isPrime(bin(i).count('1'))):
            print(i, end=' ')
            count += 1

        i += 1


# Driver Code
n = 25
printPernicious(n)

# This code is contributed by Ansu Kumari
