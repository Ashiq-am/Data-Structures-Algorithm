# Python3 program to find size of
# minimum possible array after
# removing elements according to given rules
MAX = 1000

dp = [[-1 for i in range(MAX)] for i in range(MAX)]


# dp[i][j] denotes the minimum number of elements left in
# the subarray arr[i..j].

def minSizeRec(arr, low, high, k):
    # If already evaluated
    if dp[low][high] != -1:
        return dp[low][high]

    # If size of array is less than 3
    if (high - low + 1) < 3:
        return (high - low + 1)

    # Initialize result as the case when first element is
    # separated (not removed using given rules)
    res = 1 + minSizeRec(arr, low + 1, high, k)

    # Now consider all cases when
    # first element forms a triplet
    # and removed. Check for all possible
    # triplets (low, i, j)

    for i in range(low + 1, high):

        for j in range(i + 1, high + 1):

            # Check if this triplet follows the given rules of
            # removal. And elements between 'low' and 'i' , and
            # between 'i' and 'j' can be recursively removed.
            if (arr[i] == (arr[low] + k) and arr[j] == (arr[low] + 2 * k) and
                    minSizeRec(arr, low + 1, i - 1, k) == 0 and
                    minSizeRec(arr, i + 1, j - 1, k) == 0):
                res = min(res, minSizeRec(arr, j + 1, high, k))

    # Insert value in table and return result
    dp[low][high] = res
    return res


# This function mainly initializes dp table and calls
# recursive function minSizeRec
def minSize(arr, n, k):
    dp = [[-1 for i in range(MAX)] for i in range(MAX)]
    return minSizeRec(arr, 0, n - 1, k)


# Driver program to test above function
if __name__ == '__main__':
    arr = [2, 3, 4, 5, 6, 4]
    n = len(arr)
    k = 1
    print(minSize(arr, n, k))

# this code is contributed by sahilshelangia

