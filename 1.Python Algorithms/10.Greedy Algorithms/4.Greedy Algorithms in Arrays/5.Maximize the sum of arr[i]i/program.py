# Python program to find the
# maximum value of i*arr[i]
def maxSum(arr, n):
    # Sort the array
    arr.sort()

    # Finding the sum of
    # arr[i]*i
    sum = 0
    for i in range(n):
        sum += arr[i] * i

    return sum


# Driver Program
arr = [3, 5, 6, 1]
n = len(arr)
print(maxSum(arr, n))
