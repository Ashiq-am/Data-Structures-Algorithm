''' Python program to find size of array after repeated
deletion of LIS '''

# Function to construct Maximum Sum LIS
from typing import List


def findLIS(arr: List[int], n: int) -> List[int]:
    # L[i] - The Maximum Sum Increasing
    # Subsequence that ends with arr[i]
    L = [0] * n
    for i in range(n):
        L[i] = []

    # L[0] is equal to arr[0]
    L[0].append(arr[0])

    # start from index 1
    for i in range(1, n):

        # for every j less than i
        for j in range(i):

            ''' L[i] = MaxSum(L[j]) + arr[i]
            where j < i and arr[j] < arr[i] '''
            if (arr[i] > arr[j] and
                    (len(L[i]) < len(L[j]))):
                L[i] = L[j].copy()

        # L[i] ends with arr[i]
        L[i].append(arr[i])

    # set lis = LIS
    # whose size is max among all
    maxSize = 1
    lis: List[int] = []
    for x in L:

        # The > sign makes sure that the LIS
        # ending first is chose.
        if (len(x) > maxSize):
            lis = x.copy()
            maxSize = len(x)

    return lis


# Function to minimize array
def minimize(input: List[int], n: int) -> None:
    arr = input.copy()

    while len(arr):

        # Find LIS of current array
        lis = findLIS(arr, len(arr))

        # If all elements are in decreasing order
        if (len(lis) < 2):
            break

        # Remove lis elements from current array. Note
        # that both lis[] and arr[] are sorted in
        # increasing order.
        i = 0
        while i < len(arr) and len(lis) > 0:

            # If first element of lis[] is found
            if (arr[i] == lis[0]):
                # Remove lis element from arr[]
                arr.remove(arr[i])
                i -= 1

                # Erase first element of lis[]
                lis.remove(lis[0])
            i += 1

    # print remaining element of array
    i = 0
    while i < len(arr):
        print(arr[i], end=" ")
        i += 1

    # print -1 for empty array
    if (i == 0):
        print("-1")


# Driver function
if __name__ == "__main__":
    input = [3, 2, 6, 4, 5, 1]
    n = len(input)

    # minimize array after deleting LIS
    minimize(input, n)
