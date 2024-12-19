# Python program to print all bitwise
# subsets of N (Naive approach)
def printSubsets(n):
    for i in range(n + 1):

        if ((n & i) == i):
            print(i, " ", end="")


# Driver code
n = 9
printSubsets(n)
