# Python3 program to find the two odd occurring elements

""" Prints two numbers that occur odd number of times.
The function assumes that the array size is at least 2
and there are exactly two numbers occurring odd number
of times.
"""


def printTwoOdd(arr, size):
    arr.sort()

    # Create map and calculate frequency of array
    # of elements using array.
    m = {}
    for i in range(size):
        if arr[i] not in m:
            m[arr[i]] = 0

        m[arr[i]] += 1

    """Traverse through the map and check if its second
    element that is the frequency is odd or not.Then this
    is the odd occurring element .Its is clearly mentioned
    in problem that there are only two odd occurring
    elements so this will print those two elements."""
    print("The two ODD elements are ", end="")
    for x in m:
        if (m[x] % 2 != 0):
            print(x, end=", ")


# Driver code
arr = [4, 2, 4, 5, 2, 3, 3, 1]
arr_size = len(arr)

printTwoOdd(arr, arr_size)

# This code is contributed by shubhamsingh10
