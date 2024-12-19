# Python3 program to find Noble
# elements in an array.

# Returns a Noble integer if
# present, else returns -1.
def nobleInteger(arr, size):
    for i in range(0, size):

        count = 0
        for j in range(0, size):
            if (arr[i] < arr[j]):
                count += 1
        # If count of greater
        # elements is equal
        # to arr[i]
        if (count == arr[i]):
            return arr[i]

    return -1


# Driver code
arr = [10, 3, 20, 40, 2]
size = len(arr)
res = nobleInteger(arr, size)
if (res != -1):
    print("The noble integer is ",
          res)
else:
    print("No Noble Integer Found")
