# Python 3 program to find sum of
# all sub-sequences of an array.


# Return sum of sum of all sub-sequence.
def sm(arr, n):
    ans = 0

    # Finding sum of the array.
    for i in range(0, n):
        ans = ans + arr[i]

    return ans * pow(2, n - 1)


# Driver Code
arr = [6, 7, 8]
n = len(arr)

print(sm(arr, n))

# This code is contributed by Nikita Tiwari.
