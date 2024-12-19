# Python 3 program to find a unique
# pair in an array of pairs.
def findUniquePair(arr, n):
    # XOR each element and get XOR
    # of two unique elements(ans)
    XOR = arr[0]
    for i in range(1, n):
        XOR = XOR ^ arr[i]

    # Now XOR has XOR of two missing
    # elements. Any set bit in it
    # must be set in one missing and
    # unset in other missing number

    # Get a set bit of XOR (We get
    # the rightmost set bit)
    set_bit_no = XOR & ~(XOR - 1)

    # Now divide elements in two sets
    # by comparing rightmost set bit
    # of XOR with bit at same position
    # in each element.
    x = 0
    y = 0  # Initialize missing numbers
    for i in range(0, n):

        if (arr[i] & set_bit_no):

            # XOR of first set in
            # arr[]
            x = x ^ arr[i]
        else:

            # XOR of second set
            # in arr[]
            y = y ^ arr[i]

    print("The unique pair is (", x,
          ", ", y, ")", sep="")


# Driver code
a = [6, 1, 3, 5, 1, 3, 7, 6]
n = len(a)
findUniquePair(a, n)

# This code is contributed by Smitha.
