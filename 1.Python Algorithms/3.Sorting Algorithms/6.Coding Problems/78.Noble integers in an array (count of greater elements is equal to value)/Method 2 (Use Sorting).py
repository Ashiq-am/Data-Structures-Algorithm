# Python3 code to find Noble elements
# in an array

def nobleInteger(arr):
    arr.sort()

    # Return a Noble element if
    # present before last
    n = len(arr)

    for i in range(n - 1):

        if arr[i] == arr[i + 1]:
            continue

        # In case of duplicates we reach
        # last occurrence here
        if arr[i] == n - i - 1:
            return arr[i]

    if arr[n - 1] == 0:
        return arr[n - 1]
    return -1


# Driver code
arr = [10, 3, 20, 40, 2]

res = nobleInteger(arr)

if res != -1:
    print("The noble integer is", res)
else:
    print("No Noble Integer Found")
