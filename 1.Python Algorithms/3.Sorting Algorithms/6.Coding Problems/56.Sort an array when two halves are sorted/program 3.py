# Python3 program to Merge Two Sorted
# Halves Of Array Into Single Sorted Array
def SortTwoHalfSorted(A, n):
    i = 0
    j = n // 2

    # Loop until end of array
    while (j < n):

        # If two pointer is equal then go
        # to next element of second half.
        if (i == j):
            j += 1

        # If element of first half is bigger
        # than element of second half swap two
        # elements and go next element of first half
        if (j < n and A[i] > A[j]):
            A[i], A[j] = A[j], A[i]

        i += 1


# Driver code
A = [2, 3, 8, -1, 7, 10]
n = len(A)
SortTwoHalfSorted(A, n)

# Print sorted Array
for i in range(n):
    print(A[i], end=" ")
