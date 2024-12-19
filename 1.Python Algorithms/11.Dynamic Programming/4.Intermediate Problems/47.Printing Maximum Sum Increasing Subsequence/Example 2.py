# Dynamic Programming solution to construct
# Maximum Sum Increasing Subsequence
import sys


# Function to construct and print the Maximum Sum
# Increasing Subsequence
def constructMaxSumIS(arr, n):
    # L[i] stores the value of Maximum Sum Increasing
    # Subsequence that ends with arr[i] and the index of
    # previous element used to construct the Subsequence
    L = []

    index = 0
    for i in arr:
        L.append([i, index])
        index += 1

    # Set L[0].second equal to -1
    L[0][1] = -1

    # start from index 1
    for i in range(1, n):

        # for every j less than i
        for j in range(i):
            if (arr[i] > arr[j] and L[i][0] < arr[i] + L[j][0]):
                L[i][0] = arr[i] + L[j][0]
                L[i][1] = j

    maxi, currIndex, track = -sys.maxsize, 0, 0

    for p in L:
        if (p[0] > maxi):
            maxi = p[0]
            currIndex = track

        track += 1

    # Stores the final Subsequence
    result = []

    while (currIndex >= 0):
        result.append(arr[currIndex])
        prevoiusIndex = L[currIndex][1]

        if (currIndex == prevoiusIndex):
            break

        currIndex = prevoiusIndex

    for i in range(len(result) - 1, -1, -1):
        print(result[i], end=" ")


arr = [1, 101, 2, 3, 100, 4, 5]
n = len(arr)

# Function call
constructMaxSumIS(arr, n)
