# Python 3 program to count all pairs
# with bit difference as k

# Utility function to count total
# ones in a number
def bitCount(n):
    count = 0
    while (n):
        if (n & 1):
            count += 1
        n >>= 1

    return count


# Function to count pairs of K different bits
def countPairsWithKDiff(arr, n, k):
    ans = 0

    # initialize final answer
    for i in range(0, n - 1, 1):
        for j in range(i + 1, n, 1):
            xoredNum = arr[i] ^ arr[j]

            # Check for K differ bit
            if (k == bitCount(xoredNum)):
                ans += 1

    return ans


# Driver code
if __name__ == '__main__':
    k = 2
    arr = [2, 4, 1, 3, 1]
    n = len(arr)

    print("Total pairs for k =", k, "are",
          countPairsWithKDiff(arr, n, k))

# This code is contributed by
# Sanjit_Prasad
