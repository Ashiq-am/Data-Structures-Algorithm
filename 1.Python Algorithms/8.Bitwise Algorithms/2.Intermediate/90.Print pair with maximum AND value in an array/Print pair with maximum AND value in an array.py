# Python 3 Program to find pair with
# maximum AND value

# Utility function to check number of
# elements having set msb as of pattern
def checkBit(pattern, arr, n):
    count = 0
    for i in range(0, n):
        if ((pattern & arr[i]) == pattern):
            count += 1
    return count


# Function for finding maximum and
# value pair
def maxAND(arr, n):
    res = 0

    # iterate over total of 30bits
    # from msb to lsb
    for bit in range(31, -1, -1):

        # find the count of element
        # having set msb
        count = checkBit(res | (1 << bit),
                         arr, n)

        # if count >= 2 set particular
        # bit in result
        if (count >= 2):
            res |= (1 << bit)

    # Find the elements
    if (res == 0):
        print("Not Possible")

    else:
        # print the pair of elements
        print("Pair = ", end="")

        count = 0

        i = 0
        while (i < n and count < 2):

            # inc count value after
            # printing element
            if ((arr[i] & res) == res):
                count += 1
                print(arr[i], end=" ")
            i += 1

    # return the result value
    return res


# Driver function
arr = [4, 8, 6, 2]
n = len(arr)
print("\nMaximum AND Value = ",
      maxAND(arr, n))

# This code is contributed by Smitha
