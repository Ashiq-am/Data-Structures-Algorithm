# Python program to divide n integers
# in two groups such that absolute
# difference of their sum is minimum
import math


# To print vector along size
def printVector(v):
    # Print vector size
    print(len(v))

    # Print vector elements
    for i in range(0, len(v)):
        print(v[i], end=" ")

    print()


# To divide n in two groups such that
# absolute difference of their sum is
# minimum
def findTwoGroup(n):
    # Find sum of all elements upto n
    sum = n * (n + 1) / 2

    # Sum of elements of group1
    group1Sum = sum / 2

    group1 = []
    group2 = []
    for i in range(n, 0, -1):

        # If sum is greater then or equal
        # to 0 include i in group 1
        # otherwise include in group2
        if (group1Sum - i >= 0):
            group1.append(i)

            # Decrease sum of group1
            group1Sum -= i

        else:
            group2.append(i)

    # Print both the groups
    printVector(group1)
    printVector(group2)


# driver code
n = 5
findTwoGroup(n)
