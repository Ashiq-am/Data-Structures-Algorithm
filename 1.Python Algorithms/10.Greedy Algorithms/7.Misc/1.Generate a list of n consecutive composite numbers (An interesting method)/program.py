# Python3 program to print n consecutive
# composite numbers.

# function to find factorial
# of given number
def factorial(n):
    res = 1
    for i in range(2, n + 1):
        res *= i
    return res


# Prints n consecutive numbers.
def printNComposite(n):
    fact = factorial(n + 1)
    for i in range(2, n + 2):
        print(fact + i, end=" ")


# Driver Code
n = 4
printNComposite(n)
