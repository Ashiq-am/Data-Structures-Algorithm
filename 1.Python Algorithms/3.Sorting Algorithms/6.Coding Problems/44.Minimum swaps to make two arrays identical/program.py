# Python3 program to make
# an array same to another
# using minimum number of swap

# Function returns the minimum
# number of swaps required to
# sort the array
# This method is taken from below post
# https: // www.geeksforgeeks.org/
# minimum-number-swaps-required-sort-array/
def minSwapsToSort(arr, n):
    # Create an array of pairs
    # where first element is
    # array element and second
    # element is position of
    # first element
    arrPos = [[0 for x in range(2)]
              for y in range(n)]

    for i in range(n):
        arrPos[i][0] = arr[i]
        arrPos[i][1] = i

    # Sort the array by array
    # element values to get right
    # position of every element
    # as second element of pair.
    arrPos.sort()

    # To keep track of visited
    # elements. Initialize all
    # elements as not visited
    # or false.
    vis = [False] * (n)

    # Initialize result
    ans = 0

    # Traverse array elements
    for i in range(n):

        # Already swapped and corrected or
        # already present at correct pos
        if (vis[i] or arrPos[i][1] == i):
            continue

        # Find out the number of node in
        # this cycle and add in ans
        cycle_size = 0
        j = i

        while (not vis[j]):
            vis[j] = 1

            # Move to next node
            j = arrPos[j][1]
            cycle_size += 1

        # Update answer by
        # adding current cycle.
        ans += (cycle_size - 1)

    # Return result
    return ans


# Method returns minimum
# number of swap to mak
# array B same as array A
def minSwapToMakeArraySame(a, b, n):
    # map to store position
    # of elements in array B
    # we basically store
    # element to index mapping.
    mp = {}
    for i in range(n):
        mp[b[i]] = i

    # now we're storing position
    # of array A elements
    # in array B.
    for i in range(n):
        b[i] = mp[a[i]]

    # Returing minimum swap
    # for sorting in modified
    # array B as final answer
    return minSwapsToSort(b, n)


# Driver code
if __name__ == "__main__":
    a = [3, 6, 4, 8]
    b = [4, 6, 8, 3]
    n = len(a)
    print(minSwapToMakeArraySame(a, b, n))
