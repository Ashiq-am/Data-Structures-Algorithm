# Python3 program to find the element
# occurring odd number of times

# function to find the element
# occurring odd number of times
def getOddOccurrence(arr, size):
    # Defining HashMap in C++
    Hash = dict()

    # Putting all elements into the HashMap
    for i in range(size):
        Hash[arr[i]] = Hash.get(arr[i], 0) + 1;

    # Iterate through HashMap to check an element
    # occurring odd number of times and return it
    for i in Hash:

        if (Hash[i] % 2 != 0):
            return i
    return -1


# Driver code
arr = [2, 3, 5, 4, 5, 2, 4, 3, 5, 2, 4, 4, 2]
n = len(arr)

# Function calling
print(getOddOccurrence(arr, n))

# This code is contributed by mohit kumar
