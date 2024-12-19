# Python3 program for the above approach

# Function to calculate sum of the array
def sumArray(arr, n):
    sum = 0

    # Iterate from 0 to n - 1
    for i in range(n):
        sum += arr[i]

    return sum


# Function to maximize sum
def maximizeSum(arr, n, k):
    arr.sort()
    i = 0

    # Iterate from 0 to n - 1
    for i in range(n):
        if (k and arr[i] < 0):
            arr[i] *= -1
            k -= 1
            continue

        break

    if (i == n):
        i -= 1

    if (k == 0 or k % 2 == 0):
        return sumArray(arr, n)

    if (i != 0 and abs(arr[i]) >= abs(arr[i - 1])):
        i -= 1

    arr[i] *= -1
    return sumArray(arr, n)


# Driver Code
n = 5
k = 4
arr = [-3, -2, -1, 5, 6]

# Function Call
print(maximizeSum(arr, n, k))
