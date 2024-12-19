# Python3 implementation of smallest
# difference triplet

# Function to find maximum number
def maximum(a, b, c):
    return max(max(a, b), c)


# Function to find minimum number
def minimum(a, b, c):
    return min(min(a, b), c)


# Finds and prints the smallest
# Difference Triplet
def smallestDifferenceTriplet(arr1, arr2, arr3, n):
    # sorting all the three arrays
    arr1.sort()
    arr2.sort()
    arr3.sort()

    # To store resultant three numbers
    res_min = 0
    res_max = 0
    res_mid = 0

    # pointers to arr1, arr2,
    # arr3 respectively
    i = 0
    j = 0
    k = 0

    # Loop until one array reaches to its end
    # Find the smallest difference.
    diff = 2147483647
    while (i < n and j < n and k < n):

        sum = arr1[i] + arr2[j] + arr3[k]

        # maximum number
        max = maximum(arr1[i], arr2[j], arr3[k])

        # Find minimum and increment its index.
        min = minimum(arr1[i], arr2[j], arr3[k])
        if (min == arr1[i]):
            i += 1
        elif (min == arr2[j]):
            j += 1
        else:
            k += 1

        # Comparing new difference with the
        # previous one and updating accordingly
        if (diff > (max - min)):
            diff = max - min
            res_max = max
            res_mid = sum - (max + min)
            res_min = min

    # Print result
    print(res_max, ",", res_mid, ",", res_min)


# Driver code
arr1 = [5, 2, 8]
arr2 = [10, 7, 12]
arr3 = [9, 14, 6]
n = len(arr1)
smallestDifferenceTriplet(arr1, arr2, arr3, n)

