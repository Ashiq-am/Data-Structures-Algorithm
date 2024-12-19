# Python3 program to find
# third Largest element in
# an array
import sys


def thirdLargest(arr, arr_size):
    # There should be
    # atleast three elements
    if (arr_size < 3):
        print(" Invalid Input ")
        return

    # Initialize first, second
    # and third Largest element
    first = arr[0]
    second = -sys.maxsize
    third = -sys.maxsize

    # Traverse array elements
    # to find the third Largest
    for i in range(1, arr_size):

        # If current element is
        # greater than first,
        # then update first,
        # second and third
        if (arr[i] > first):

            third = second
            second = first
            first = arr[i]


        # If arr[i] is in between
        # first and second
        elif (arr[i] > second):

            third = second
            second = arr[i]

        # If arr[i] is in between
        # second and third
        elif (arr[i] > third):
            third = arr[i]

    print("The third Largest",
          "element is", third)


# Driver Code
arr = [12, 13, 1,
       10, 34, 16]
n = len(arr)
thirdLargest(arr, n)


