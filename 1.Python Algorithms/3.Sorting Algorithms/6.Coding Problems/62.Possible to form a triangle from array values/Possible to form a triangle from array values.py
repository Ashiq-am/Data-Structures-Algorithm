# Python3 code to find if
# it is possible to form a
# triangle from array values

# Method prints possible
# triangle when array
# values are taken as sides
def isPossibleTriangle(arr, N):
    # If number of elements
    # are less than 3, then
    # no triangle is possible
    if N < 3:
        return False

    # first sort the array
    arr.sort()

    # loop for all 3
    # consecutive triplets
    for i in range(N - 2):

        # If triplet satisfies triangle
        # condition, break
        if arr[i] + arr[i + 1] > arr[i + 2]:
            return True


# Driver Code
arr = [5, 4, 3, 1, 2]
N = len(arr)
print("Yes" if isPossibleTriangle(arr, N) else "No")
