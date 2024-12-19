# Python3 program to implement
# simple approach to sort
# an array according to
# count of set bits.

# Function to count setbits
def setBitCount(num):
    count = 0

    while (num):
        if (num & 1):
            count += 1

        num = num >> 1

    return count


# Function to sort By SetBitCount
def sortBySetBitCount(arr, n):
    count = []

    # Iterate over all values and
    # insert into multimap
    for i in range(n):
        count.append([(-1) *
                      setBitCount(arr[i]), arr[i]])

    count.sort(key=lambda x: x[0])

    for i in range(len(count)):
        print(count[i][1], end=" ")


# Driver Code
arr = [1, 2, 3, 4, 5, 6]
n = len(arr)

sortBySetBitCount(arr, n)
