# Python3 program to implement the approach
def rec(i, x, arr, size):
    # return the current xor sum if we reach the end of
    # array
    if (i == size):
        return x

    # first choice can be to include the i-th element in
    # the subset and thus we take its xor
    choice1 = rec(i + 1, x ^ arr[i], arr, size)

    # second choice can be to include the i-th element in
    # the subset and thus we take its xor
    choice2 = rec(i + 1, x, arr, size)

    # return sum of both the choices as we need to find the
    # sum of xor of all subsets
    return choice1 + choice2


# Returns sum of XORs of all subsets
def xorSum(arr, size):
    return rec(0, 0, arr, size)


# Driver code
arr = [1, 5, 6]
size = len(arr)

# Function call
print(xorSum(arr, size))

# This code is contributed by phasing17
