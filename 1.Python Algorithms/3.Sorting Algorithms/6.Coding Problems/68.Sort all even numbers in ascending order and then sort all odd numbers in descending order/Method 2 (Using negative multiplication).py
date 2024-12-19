# Python 3 program to sort array in
# even and odd manner. The odd
# numkbers are to be sorted in
# descending order and the even
# numbers in ascending order

# To do two way sort. First sort
# even numbers in ascending order,
# then odd numbers in descending order.
def twoWaySort(arr, n):
    # Make all odd numbers negative
    for i in range(0, n):

        # Check for odd
        if (arr[i] & 1):
            arr[i] *= -1

    # Sort all numbers
    arr.sort()

    # Retaining original array
    for i in range(0, n):
        if (arr[i] & 1):
            arr[i] *= -1


# Driver code
arr = [1, 3, 2, 7, 5, 4]
n = len(arr)
twoWaySort(arr, n)
for i in range(0, n):
    print(arr[i], end=" ")

