# Python3 Program to find SOP of all combination
# taken (1 to N) at a time using brute force

# to store sum of every combination
def Combination(a, combi, n, r, depth, index):
    global Sum

    # if we have reached sufficient depth
    if index == r:

        # find the product of combination
        product = 1
        for i in range(r):
            product = product * combi[i]

        # add the product into sum
        Sum += product
        return

    # recursion to produce different
    # combination
    for i in range(depth, n):
        combi[index] = a[i]
        Combination(a, combi, n, r,
                    i + 1, index + 1)


# function to print sum of products of
# all combination taken 1-N at a time
def allCombination(a, n):
    global Sum
    for i in range(1, n + 1):
        # creating temporary array for
        # storing combination
        combi = [0] * i

        # call combination with r = i
        # for combination taken i at a time
        Combination(a, combi, n, i, 0, 0)

        # displaying sum
        print("f(", i, ") --> ", Sum)
        Sum = 0


# Driver Code
Sum = 0
n = 5
a = [0] * n

# storing numbers from 1-N in array
for i in range(n):
    a[i] = i + 1

# calling allCombination
allCombination(a, n)
