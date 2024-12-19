# Python program for the above approach
from collections import Counter


# Function to return the sum of distinct elements
def sumOfElements(arr, n):
    # Counter function is used to
    # calculate frequency of elements of array
    freq = Counter(arr)

    # Converting keys of freq dictionary to list
    lis = list(freq.keys())

    # Return sum of list
    return sum(lis)


# Driver code
if __name__ == "__main__":
    arr = [1, 2, 3, 1, 1, 4, 5, 6]
    n = len(arr)

    print(sumOfElements(arr, n))
