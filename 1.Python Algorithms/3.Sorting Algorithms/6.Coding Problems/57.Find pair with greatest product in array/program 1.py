# Python 3 program to find a pair
# with product in given array.

# Function to find greatest number
def findGreatest(arr, n):
    result = -1
    for i in range(n):
        for j in range(n - 1):
            for k in range(j + 1, n):
                if (arr[j] * arr[k] == arr[i]):
                    result = max(result, arr[i])
    return result


# Driver code
if __name__ == "__main__":
    arr = [30, 10, 9, 3, 35]
    n = len(arr)

    print(findGreatest(arr, n))
