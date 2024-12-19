# Python code to count the number of ordered
# pairs satisfying Line Equation

# Checks if (i, j) is valid, a point (i, j)
# is valid if point (arr[i], arr[j])
# satisfies the equation y = mx + c And
# i is not equal to j
def isValid(arr, i, j, m, c):
    # check if i equals to j
    if (i == j):
        return False

    # Equation LHS = y, and RHS = mx + c
    lhs = arr[j]
    rhs = m * arr[i] + c

    return (lhs == rhs)


# Returns the number of ordered pairs
# (i, j) for which point (arr[i], arr[j])
# satisfies the equation of the line
# y = mx + c */
def findOrderedPoints(arr, n, m, c):
    counter = 0

    # for every possible (i, j) check
    # if (a[i], a[j]) satisfies the
    # equation y = mx + c
    for i in range(0, n):
        for j in range(0, n):
            # (firstIndex, secondIndex)
            # is same as (i, j)
            firstIndex = i
            secondIndex = j

            # check if (firstIndex,
            # secondIndex) is a valid point
            if (isValid(arr, firstIndex,
                        secondIndex, m, c)):
                counter = counter + 1

    return counter


# Driver Code
arr = [1, 2, 3, 4, 2]
n = len(arr)

# equation of line is y = mx + c
m = 1
c = 1
print(findOrderedPoints(arr, n, m, c))

# This code is contributed by Manish Shaw
# (manishshaw1)
