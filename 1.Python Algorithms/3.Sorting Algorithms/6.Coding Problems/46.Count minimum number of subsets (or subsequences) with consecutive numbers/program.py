# Python program to find number of subset containing
# consecutive numbers
def numofsubset(arr, n):
    # Sort the array so that elements which are consecutive
    # in nature became consecutive in the array.
    x = sorted(arr)


    count = 1



    for i in range(0, n-1):

        # Check if there is beginning of another subset of
        # consecutive number
        if (x[i] + 1 != x[i + 1]):
            count = count + 1


    return count

# Driven Program
arr = [ 100, 56, 5, 6, 102, 58, 101, 57, 7, 103, 59 ]
n = len(arr)
print(numofsubset(arr, n))
