# Python program to find
# lexicographically
# maximum value after
# k swaps.

arr = [3, 5, 4, 1, 2]


# Function which
# modifies the array
def KSwapMaximum(n, k):
    global arr
    for i in range(0, n - 1):
        if (k > 0):

            # Here, indexPosition
            # is set where we want to
            # put the current largest
            # integer
            indexPosition = i
            for j in range(i + 1, n):

                # If we exceed the Max swaps
                # then break the loop
                if (k <= j - i):
                    break

                # Find the maximum value
                # from i+1 to max k or n
                # which will replace
                # arr[indexPosition]
                if (arr[j] > arr[indexPosition]):
                    indexPosition = j

            # Swap the elements from
            # Maximum indexPosition
            # we found till now to
            # the ith index
            for j in range(indexPosition, i, -1):
                t = arr[j]
                arr[j] = arr[j - 1]
                arr[j - 1] = t

            # Updates k after swapping
            # indexPosition-i elements
            k = k - indexPosition - i


# Driver code
n = len(arr)
k = 3

KSwapMaximum(n, k)

# Print the final Array
for i in range(0, n):
    print("{} ".format(arr[i]),end="")
