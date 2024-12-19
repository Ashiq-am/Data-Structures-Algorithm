# Python3 program to find the
# two odd occurring elements

# Prints two numbers that occur odd
# number of times. The function assumes
# that the array size is at least 2 and
# there are exactly two numbers occurring
# odd number of times.
def printTwoOdd(arr, size):
    # Will hold XOR of two odd occurring elements
    xor2 = arr[0]

    # Will have only single set bit of xor2
    set_bit_no = 0
    n = size - 2
    x, y = 0, 0

    # Get the xor of all elements in arr[].
    # The xor will basically be xor of two
    # odd occurring elements
    for i in range(1, size):
        xor2 = xor2 ^ arr[i]

    # Get one set bit in the xor2. We get
    # rightmost set bit in the following
    # line as it is easy to get
    set_bit_no = xor2 & ~(xor2 - 1)

    # Now divide elements in two sets:
    # 1) The elements having the corresponding bit as 1.
    # 2) The elements having the corresponding bit as 0.
    for i in range(size):

        # XOR of first set is finally going to
        # hold one odd occurring number x
        if (arr[i] & set_bit_no):
            x = x ^ arr[i]

        # XOR of second set is finally going
        # to hold the other odd occurring number y
        else:
            y = y ^ arr[i]

    print("The two ODD elements are", x, "&", y)


# Driver Code
arr = [4, 2, 4, 5, 2, 3, 3, 1]
arr_size = len(arr)
printTwoOdd(arr, arr_size)

# This code is contributed by Anant Agarwal.
