# Python3 program to separately sort
# even-placed and odd placed numbers
# and place them together in sorted array.
def bitonicGenerator(arr, n):
    # create evenArr[] and oddArr[]
    evenArr = []
    oddArr = []

    # Put elements in oddArr[] and evenArr[]
    # as per their position
    for i in range(n):
        if ((i % 2) == 0):
            evenArr.append(arr[i])
        else:
            oddArr.append(arr[i])

        # sort evenArr[] in ascending order
    # sort oddArr[] in descending order
    evenArr = sorted(evenArr)
    oddArr = sorted(oddArr)
    oddArr = oddArr[::-1]

    i = 0
    for j in range(len(evenArr)):
        arr[i] = evenArr[j]
        i += 1
    for j in range(len(oddArr)):
        arr[i] = oddArr[j]
        i += 1


# Driver Code
arr = [1, 5, 8, 9, 6, 7, 3, 4, 2, 0]
n = len(arr)
bitonicGenerator(arr, n)
for i in arr:
    print(i, end=" ")
