# Finding peak element in a 2D Array.
MAX = 100
from math import ceil


# Function to find the maximum in column 'mid'
# 'rows' is number of rows.
def findMax(arr, rows, mid, max):
    max_index = 0
    for i in range(rows):
        if (max < arr[i][mid]):
            # Saving global maximum and its index
            # to check its neighbours
            max = arr[i][mid]
            max_index = i
        # print(max_index)

    return max, max_index


# Function to find a peak element
def findPeakRec(arr, rows, columns, mid):
    # Evaluating maximum of mid column.
    # Note max is passed by reference.
    max = 0
    max, max_index = findMax(arr, rows, mid, max)

    # If we are on the first or last column,
    # max is a peak
    if (mid == 0 or mid == columns - 1):
        return max

    # If mid column maximum is also peak
    if (max >= arr[max_index][mid - 1] and
            max >= arr[max_index][mid + 1]):
        return max

    # If max is less than its left
    if (max < arr[max_index][mid - 1]):
        return findPeakRec(arr, rows, columns,
                           mid - ceil(mid / 2.0))

    # If max is less than its left
    # if (max < arr[max_index][mid+1])
    return findPeakRec(arr, rows, columns,
                       mid + ceil(mid / 2.0))


# A wrapper over findPeakRec()
def findPeak(arr, rows, columns):
    return findPeakRec(arr, rows,
                       columns, columns // 2)


# Driver Code
arr = [[10, 8, 10, 10],
       [14, 13, 12, 11],
       [15, 9, 11, 21],
       [16, 17, 19, 20]]

# Number of Columns
rows = 4
columns = 4
print(findPeak(arr, rows, columns))
