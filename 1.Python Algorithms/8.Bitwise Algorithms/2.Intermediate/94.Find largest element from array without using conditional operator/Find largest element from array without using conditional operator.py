# Python3 Program to find largest
# element from array
import math as mt


# Utility function to check number of
# elements having set msb as of pattern
def checkBit(pattern, arr, n):
    count = 0
    for i in range(n):
        if ((pattern & arr[i]) == pattern):
            count += 1
    return count


# Function for finding maximum
# and value pair
def largest(arr, n):
    # Create a vector of given array
    v = arr

    # Insert max value of Int and update n
    v.append(2 ** 31 - 1)
    n = n + 1

    res = 0

    # Iterate over total of 30bits
    # from msb to lsb
    for bit in range(31, -1, -1):

        # Find the count of element
        # having set msb
        count = checkBit(res | (1 << bit), v, n)

        # if count | 1 != 1 set particular
        # bit in result
        if ((count | 1) != 1):
            res |= (1 << bit)

    return res


# Driver Code
arr = [4, 8, 6, 2]
n = len(arr)
print("Largest element =", largest(arr, n))

# This code is contributed by
# Mohit kumar 29
