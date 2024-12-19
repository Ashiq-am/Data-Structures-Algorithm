# Python program to calculate
# longest alternating
# sub-array for each index elements

# Function to calculate alternating sub-
# array for each index of array elements
def alternateSubarray(arr, n):
    len = []
    for i in range(n + 1):
        len.append(0)

    # Initialize the base state of len[]
    len[n - 1] = 1

    # Calculating value for each element
    for i in range(n - 2, -1, -1):

        # If both elements are different
        # then add 1 to next len[i+1]
        if (arr[i] ^ arr[i + 1] == True):
            len[i] = len[i + 1] + 1

        # else initialize to 1
        else:
            len[i] = 1

    # Print lengths of binary subarrays.
    for i in range(n):
        print(len[i], " ", end="")


# Driver code

arr = [True, False, True, False, False, True]
n = len(arr)

alternateSubarray(arr, n)


