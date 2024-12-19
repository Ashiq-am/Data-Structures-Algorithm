# Python 3 program to calculate longest
# alternating sub-array for each index elements

# Function to calculate alternating sub-array
# for each index of array elements
def alternateSubarray(arr, n):
    # Initialize count variable for
    # storing length of sub-array
    count = 1

    # Initialize 'prev' variable which
    # indicates the previous element
    # while traversing for index 'i'
    prev = arr[0]
    for i in range(1, n):

        # If both elements are same, print
        # elements because alternate element
        # is not found for current index
        if ((arr[i] ^ prev) == 0):

            # print count and decrement it.
            while (count):
                print(count, end=" ")
                count -= 1

        # Increment count for next element
        count += 1

        # Re-initialize previous variable
        prev = arr[i]

    # If elements are still available after
    # traversing whole array, print it
    while (count):
        print(count, end=" ")
        count -= 1


# Driver Code
if __name__ == '__main__':
    arr = [1, 0, 1, 0, 0, 1]
    n = len(arr)
    alternateSubarray(arr, n)
