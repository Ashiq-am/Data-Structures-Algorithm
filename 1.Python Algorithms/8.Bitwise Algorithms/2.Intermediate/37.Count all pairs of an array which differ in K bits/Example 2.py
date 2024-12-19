# Below is Python3 approach of finding
# total k bit difference pairs

# Function to calculate K bit different
# pairs in array
def kBitDifferencePairs(arr, n, k):
    # Get the maximum value among
    # all array elements
    MAX = max(arr)

    # Set the count array to 0, count[] stores
    # the total frequency of array elements
    count = [0 for i in range(MAX + 1)]

    for i in range(n):
        count[arr[i]] += 1

    # Initialize result
    ans = 0

    # For 0 bit answer will be total
    # count of same number
    if (k == 0):
        for i in range(MAX + 1):
            ans += (count[i] * (count[i] - 1)) // 2

        return ans

    for i in range(MAX + 1):

        # if count[i] is 0, skip the next loop
        # as it will not contribute the answer
        if (count[i] == 0):
            continue

        for j in range(i + 1, MAX + 1):

            # Update answer if k differ bit found
            if (bin(i ^ j).count('1') == k):
                ans += count[i] * count[j]

    return ans


# Driver code
k = 2
arr = [2, 4, 1, 3, 1]
n = len(arr)

print("Total pairs for k =", k, "are",
      kBitDifferencePairs(arr, n, k))

k = 3
print("Total pairs for k =", k, "are",
      kBitDifferencePairs(arr, n, k))

# This code is contributed by mohit kumar
