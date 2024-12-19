# Python3 implementation to find the longest
# increasing odd even subsequence

# function to find the longest
# increasing odd even subsequence
def longOddEvenIncSeq(arr, n):
    # lioes[i] stores longest increasing odd
    # even subsequence ending at arr[i]
    lioes = list()

    # to store the length of longest increasing
    # odd even subsequence
    maxLen = 0

    # Initialize LIOES values for all indexes
    for i in range(n):
        lioes.append(1)

    # Compute optimized LIOES values
    # in bottom up manner
    i = 1
    for i in range(n):
        for j in range(i):
            if (arr[i] > arr[j] and
                    (arr[i] + arr[j]) % 2 != 0 and
                    lioes[i] < lioes[j] + 1):
                lioes[i] = lioes[j] + 1

    # Pick maximum of all LIOES values
    for i in range(n):
        if maxLen < lioes[i]:
            maxLen = lioes[i]

    # required maximum length
    return maxLen


# Driver to test above
arr = [1, 12, 2, 22, 5, 30, 31, 14, 17, 11]
n = len(arr)
print("Longest Increasing Odd Even " +
      "Subsequence: ", longOddEvenIncSeq(arr, n))
