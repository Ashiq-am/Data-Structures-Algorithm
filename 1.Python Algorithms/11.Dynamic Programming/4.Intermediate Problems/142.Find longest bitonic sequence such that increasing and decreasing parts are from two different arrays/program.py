# Python3 to find largest bitonic sequence such that
res = []


# utility Binary search
def GetCeilIndex(arr, T, l, r, key):
    while (r - l > 1):
        m = l + (r - l) // 2;
        if (arr[T[m]] >= key):
            r = m
        else:
            l = m
    return r


# function to find LIS in reverse form
def LIS(arr, n):
    # Add boundary case, when array n is zero
    # Depend on smart pointers
    tailIndices = [0] * (n)  # Initialized with 0
    prevIndices = [-1] * (n)  # initialized with -1

    leN = 1  # it will always poto empty location
    for i in range(1, n):

        # new smallest value
        if (arr[i] < arr[tailIndices[0]]):
            tailIndices[0] = i

        # arr[i] wants to extend largest subsequence
        elif (arr[i] > arr[tailIndices[leN - 1]]):
            prevIndices[i] = tailIndices[leN - 1]
            tailIndices[leN] = i
            leN += 1

        # arr[i] wants to be a potential candidate of
        # future subsequence
        # It will replace ceil value in tailIndices
        else:
            pos = GetCeilIndex(arr, tailIndices, -1,
                               leN - 1, arr[i])
            prevIndices[i] = tailIndices[pos - 1]
            tailIndices[pos] = i

    # put LIS into vector
    i = tailIndices[leN - 1]
    while (i >= 0):
        # print(i)
        res.append(arr[i])
        i = prevIndices[i]


# function for finding longest bitonic seq
def longestBitonic(arr1, n1, arr2, n2):
    global res

    # find LIS of array 1 in reverse form
    LIS(arr1, n1)

    # reverse res to get LIS of first array
    res = res[::-1]

    # reverse array2 and find its LIS
    arr2 = arr2[::-1]
    LIS(arr2, n2)

    # print result
    for i in res:
        print(i, end=" ")


# Driver program

arr1 = [1, 2, 4, 3, 2]
arr2 = [8, 6, 4, 7, 8, 9]
n1 = len(arr1)
n2 = len(arr2)
longestBitonic(arr1, n1, arr2, n2)
