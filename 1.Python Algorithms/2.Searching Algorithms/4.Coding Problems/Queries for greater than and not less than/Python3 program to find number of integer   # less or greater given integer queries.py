# Python3 program to find number of integer
# less or greater given integer queries

# Return the index of integer
# which are not less than x
# (or greater than or equal to x)
def lower_bound(arr, start, end, x):
    while (start < end):

        mid = (start + end) >> 1
        if (arr[mid] >= x):
            end = mid
        else:
            start = mid + 1

    return start


# Return the index of integer
# which are greater than x.
def upper_bound(arr, start, end, x):
    while (start < end):

        mid = (start + end) >> 1
        if (arr[mid] <= x):
            start = mid + 1
        else:
            end = mid

    return start


def query(arr, n, type, x):
    # Counting number of integer
    # which are greater than x.
    if (type == 1):
        print(n - upper_bound(arr, 0, n, x))

    # Counting number of integer
    # which are not less than x
    # (Or greater than or equal to x)
    else:
        print(n - lower_bound(arr, 0, n, x))

    # Driver code


arr = [1, 2, 3, 4]
n = len(arr)

arr.sort()

query(arr, n, 0, 5)
query(arr, n, 1, 3)
query(arr, n, 0, 3)
