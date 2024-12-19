# Python3 program to check if a given array
# can form arithmetic progression

# Returns true if a permutation of arr[0..n-1]
# can form arithmetic progression
def checkIsAP(arr, n):
    hm = {}
    smallest = float('inf')
    second_smallest = float('inf')

    for i in range(n):

        # Find the smallest and and
        # update second smallest
        if (arr[i] < smallest):
            second_smallest = smallest
            smallest = arr[i]

        # Find second smallest
        elif (arr[i] != smallest and
              arr[i] < second_smallest):
            second_smallest = arr[i]

        # Check if the duplicate element found or not
        if arr[i] not in hm:
            hm[arr[i]] = 1

        # If duplicate found then return false
        else:
            return False

    # Find the difference between smallest
    # and second smallest
    diff = second_smallest - smallest

    # As we have used smallest and
    # second smallest,so we
    # should now only check for n-2 elements
    for i in range(n - 1):
        if (second_smallest) not in hm:
            return False

        second_smallest += diff

    return True


# Driver code
arr = [20, 15, 5, 0, 10]
n = len(arr)

if (checkIsAP(arr, n)):
    print("Yes")
else:
    print("No")
