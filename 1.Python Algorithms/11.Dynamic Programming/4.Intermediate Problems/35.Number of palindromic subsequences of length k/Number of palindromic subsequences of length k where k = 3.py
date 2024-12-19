# Python3 program to count number of
# subsequences of given length.

MAX = 100
MAX_CHAR = 26


# Precompute the prefix and suffix array.
def precompute(s, n, l, r):
    l[ord(s[0]) - ord('a')][0] = 1

    # Precompute the prefix 2D array
    for i in range(1, n):
        for j in range(MAX_CHAR):
            l[j][i] += l[j][i - 1]

        l[ord(s[i]) - ord('a')][i] += 1

    r[ord(s[n - 1]) - ord('a')][n - 1] = 1

    # Precompute the Suffix 2D array.
    k = n - 2
    while (k >= 0):
        for j in range(MAX_CHAR):
            r[j][k] += r[j][k + 1]
        r[ord(s[k]) - ord('a')][k] += 1
        k -= 1


# Find the number of palindromic
# subsequence of length k
def countPalindromes(k, n, l, r):
    ans = 0

    # If k is 1.
    if (k == 1):
        for i in range(MAX_CHAR):
            ans += l[i][n - 1]
        return ans

    # If k is 2
    if (k == 2):

        # Adding all the products of
        # prefix array
        for i in range(MAX_CHAR):
            ans += ((l[i][n - 1] * (l[i][n - 1] - 1)) / 2)
        return ans

    # For k greater than 2. Adding all
    # the products of value of prefix
    # and suffix array.
    for i in range(1, n - 1):
        for j in range(MAX_CHAR):
            ans += l[j][i - 1] * r[j][i + 1]
    return ans


# Driven Program
s = "aabab"
k = 2
n = len(s)

l = [[0 for x in range(MAX)] for y in range(MAX_CHAR)]
r = [[0 for x in range(MAX)] for y in range(MAX_CHAR)]

precompute(s, n, l, r)
print(countPalindromes(k, n, l, r))
