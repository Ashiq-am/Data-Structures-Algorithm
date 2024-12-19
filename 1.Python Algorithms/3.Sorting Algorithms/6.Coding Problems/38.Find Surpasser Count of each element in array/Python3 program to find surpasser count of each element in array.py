# Naive Python3 program to find
# surpasser count of each element in array

# Function to find surpasser count of
# each element in array
def findSurpasser(arr, n):
    for i in range(0, n):

        # stores surpasser count for element
        # arr[i]
        count = 0

        for j in range(i + 1, n):
            if (arr[j] > arr[i]):
                count += 1

        print(count, end=" ")


# Function to print an array
def printArray(arr, n):
    for i in range(0, n):
        print(arr[i], end=" ")


# Driver program to test above functions
arr = [2, 7, 5, 3, 0, 8, 1]
n = len(arr)

print("Given array is")
printArray(arr, n)

print("\nSurpasser Count of array is")
findSurpasser(arr, n)
