# Python3 program to find two Missing Numbers using O(n)
# extra space

# Function to find two missing numbers in range
# [1, n]. This function assumes that size of array
# is n-2 and all array elements are distinct
def findTwoMissingNumbers(arr, n):
    # Create a boolean vector of size n+1 and
    # mark all present elements of arr[] in it.
    mark = [False for i in range(n + 1)]
    for i in range(0, n - 2, 1):
        mark[arr[i]] = True

    # Print two unmarked elements
    print("Two Missing Numbers are")
    for i in range(1, n + 1, 1):
        if (mark[i] == False):
            print(i, end=" ")

    print("\n")


# Driver program to test above function
if __name__ == '__main__':
    arr = [1, 3, 5, 6]

    # Range of numbers is 2 plus size of array
    n = 2 + len(arr)

    findTwoMissingNumbers(arr, n);

# This code is contributed by
# Surendra_Gangwar
