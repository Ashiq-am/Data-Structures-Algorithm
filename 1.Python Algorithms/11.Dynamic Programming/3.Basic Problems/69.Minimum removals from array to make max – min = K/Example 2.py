# Python program for the
# above approach

# Function to find
# rightmost index
# which satisfies the condition
# arr[j] - arr[i] <= k
def findInd(key, i, n,
            k, arr):
    ind = -1

    # Initialising start
    # to i + 1
    start = i + 1

    # Initialising end
    # to n - 1
    end = n - 1;

    # Binary search implementation
    # to find the rightmost element
    # that satisfy the condition
    while (start < end):
        mid = int(start +
                  (end - start) / 2)

        # Check if the condition
        # satisfies
        if (arr[mid] - key <= k):

            # Store the position
            ind = mid

            # Make start = mid + 1
            start = mid + 1
        else:
            # Make end = mid
            end = mid

    # Return the rightmost position
    return ind


# Function to calculate
# minimum number of elements
# to be removed
def removals(arr, n, k):
    ans = n - 1

    # Sort the given array
    arr.sort()

    # Iterate from 0 to n-1
    for i in range(0, n):

        # Find j such that
        # arr[j] - arr[i] <= k
        j = findInd(arr[i], i,
                    n, k, arr)

        # If there exist such j
        # that satisfies the condition
        if (j != -1):
            # Number of elements
            # to be removed for this
            # particular case is
            # (j - i + 1)
            ans = min(ans, n -
                      (j - i + 1))

    # Return answer
    return ans


# Driver Code
a = [1, 3, 4, 9,
     10, 11, 12, 17, 20]
n = len(a)
k = 4
print(removals(a, n, k))
