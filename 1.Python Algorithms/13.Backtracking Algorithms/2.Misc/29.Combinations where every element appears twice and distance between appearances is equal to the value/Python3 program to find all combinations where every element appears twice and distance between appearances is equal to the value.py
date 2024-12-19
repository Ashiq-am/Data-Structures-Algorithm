# Python3 program to find all combinations
# where every element appears twice and distance
# between appearances is equal to the value

# Find all combinations that
# satisfies given constraints
def allCombinationsRec(arr, elem, n):
    # if all elements are filled,
    # print the solution
    if (elem > n):

        for i in (arr):
            print(i, end=" ")

        print("")
        return

    # Try all possible combinations
    # for element elem
    for i in range(0, 2 * n):

        # if position i and (i+elem+1) are
        # not occupied in the vector
        if (arr[i] == -1 and
                (i + elem + 1) < 2 * n and
                arr[i + elem + 1] == -1):
            # place elem at position
            # i and (i+elem+1)
            arr[i] = elem
            arr[i + elem + 1] = elem

            # recurse for next element
            allCombinationsRec(arr, elem + 1, n)

            # backtrack (remove elem from
            # position i and (i+elem+1) )
            arr[i] = -1
            arr[i + elem + 1] = -1


def allCombinations(n):
    # create a vector of double
    # the size of given number with
    arr = [-1] * (2 * n)

    # all its elements initialized by 1
    elem = 1

    # start from element 1
    allCombinationsRec(arr, elem, n)


# Driver code
n = 3
allCombinations(n)

# This code is contributed by Smitha Dinesh Semwal.
