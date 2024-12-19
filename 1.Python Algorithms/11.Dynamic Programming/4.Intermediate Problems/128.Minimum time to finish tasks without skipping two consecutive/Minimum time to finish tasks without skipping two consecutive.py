# Python3 program to find minimum
# time to finish tasks such that no
# two consecutive tasks are skipped.

# arr[] represents time
# taken by n given tasks
def minTime(arr, n):
    # Corner Cases
    if (n <= 0): return 0

    # Initialize value for the
    # case when there is only
    # one task in task list.
    incl = arr[0]  # First task is included
    excl = 0  # First task is exluded

    # Process remaining n-1 tasks
    for i in range(1, n):
        # Time taken if current task is included
        # There are two possibilities
        # (a) Previous task is also included
        # (b) Previous task is not included
        incl_new = arr[i] + min(excl, incl)

        # Time taken when current task is not
        # included. There is only one possibility
        # that previous task is also included.
        excl_new = incl

        # Update incl and excl for next iteration
        incl = incl_new
        excl = excl_new

    # Return maximum of two values for last task
    return min(incl, excl)


# Driver code
arr1 = [10, 5, 2, 7, 10]
n1 = len(arr1)
print(minTime(arr1, n1))

arr2 = [10, 5, 7, 10]
n2 = len(arr2)
print(minTime(arr2, n2))

arr3 = [10, 5, 2, 4, 8, 6, 7, 10]
n3 = len(arr3)
print(minTime(arr3, n3))
