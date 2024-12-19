# Python 3 program to find the even
# occurring elements in given array

# Function to find the even occurring
# elements in given array
def printRepeatingEven(arr, n):
    axor = 0;

    # do for each element of array
    for i in range(0, n):
        # left-shift 1 by value of
        # current element
        pos = 1 << arr[i];

        # Toggle the bit every time
        # element gets repeated
        axor ^= pos;

    # Traverse array again and use _xor
    # to find even occurring elements
    for i in range(0, n - 1):

        # left-shift 1 by value of
        # current element
        pos = 1 << arr[i];

        # Each 0 in _xor represents an
        # even occurrence
        if (not (pos & axor)):
            # print the even occurring numbers
            print(arr[i], end=" ");

            # set bit as 1 to avoid printing
            # duplicates
            axor ^= pos;


# Driver code
arr = [9, 12, 23, 10, 12, 12,
       15, 23, 14, 12, 15];
n = len(arr);
printRepeatingEven(arr, n);

# This code is contributed
# by Shivi_Aggarwal
