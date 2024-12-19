# Python3 program to sort an
# array after applying equation
# A*x*x + B*x + C
import sys


# Function to sort an array
# after applying given equation.
def sortArray(arr, n, A, B, C):
    # Apply equation on all elements
    for i in range(n):
        arr[i] = (A * arr[i] * arr[i] +
                  B * arr[i] + C)
    index = -(sys.maxsize - 1)
    maximum = -(sys.maxsize - 1)

    # Find maximum element in
    # resultant array
    for i in range(n):
        if maximum < arr[i]:
            index = i
            maximum = arr[i]

    # Use maximum element as a break point
    # and merge both subarrays usin simple
    # merge function of merge sort
    i = 0;
    j = n - 1;
    new_arr = [0] * n
    k = 0
    while i < index and j > index:
        if arr[i] < arr[j]:
            new_arr[k] = arr[i]
            k += 1
            i += 1
        else:
            new_arr[k] = arr[j]
            k += 1
            j -= 1

    # Merge remaining elements
    while i < index:
        new_arr[k] = arr[i]
        k += 1
        i += 1

    # Modify original array
    while j > index:
        new_arr[k] = arr[j]
        k += 1
        j -= 1
        new_arr[n - 1] = maximum

    for i in range(n):
        arr[i] = new_arr[i]


# Driver code
arr = [-21, -15, 12, 13, 14]
n = len(arr)
A = -6
B = -7
C = 2
sortArray(arr, n, A, B, C)
print("Array after sorting is:")
for i in range(n):
    print(arr[i], end=" ")
