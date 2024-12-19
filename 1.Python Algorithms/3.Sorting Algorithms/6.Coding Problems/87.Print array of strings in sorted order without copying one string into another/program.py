# Python 3 implementation to print array
# of strings in sorted order without
# copying one string into another

# function to print strings in sorted order
def printInSortedOrder(arr, n):
    index = [0] * n

    # Initially the index of the strings
    # are assigned to the 'index[]'
    for i in range(n):
        index[i] = i

    # selection sort technique is applied
    for i in range(n - 1):
        min = i
        for j in range(i + 1, n):

            # with the help of 'index[]'
            # strings are being compared
            if (arr[index[min]] > arr[index[j]]):
                min = j

        # index of the smallest string is placed
        # at the ith index of 'index[]'
        if (min != i):
            index[min], index[i] = index[i], index[min]

    # printing strings in sorted order
    for i in range(n):
        print(arr[index[i]], end=" ")


# Driver Code
if __name__ == "__main__":
    arr = ["geeks", "quiz", "geeks", "for"]
    n = 4
    printInSortedOrder(arr, n)
