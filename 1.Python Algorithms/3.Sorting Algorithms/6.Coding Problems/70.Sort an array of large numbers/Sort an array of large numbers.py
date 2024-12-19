# Python3 program to sort large numbers
# represented as strings

# Function for sort an array of large
# numbers represented as strings
def sortLargeNumbers(arr, n):
    arr.sort(key=int)


# Driver Code
if __name__ == '__main__':

    arr = ["5", "1237637463746732323",
           "97987", "12"]
    n = len(arr)

    sortLargeNumbers(arr, n)

    for i in arr:
        print(i, end=' ')
