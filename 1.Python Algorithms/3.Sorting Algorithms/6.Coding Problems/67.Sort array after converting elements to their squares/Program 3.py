# Python3 program to Sort square of the numbers of the array

# function to sort array after doing squares of elements
def sortSquares(arr, n):
    left, right = 0, n - 1
    index = n - 1
    result = [0 for x in arr]

    while index >= 0:

        if abs(arr[left]) >= abs(arr[right]):
            result[index] = arr[left] * arr[left]
            left += 1
        else:
            result[index] = arr[right] * arr[right]
            right -= 1
        index -= 1

    for i in range(n):
        arr[i] = result[i]


# Driver code
arr = [-6, -3, -1, 2, 4, 5]
n = len(arr)

print("Before sort ")
for i in range(n):
    print(arr[i], end=" ")

sortSquares(arr, n)
print("\nAfter Sort ")
for i in range(n):
    print(arr[i], end=" ")
