# Python 3 program to shuffle an array
# in O(n) time and O(1) extra space

# Shuffles an array of size 2n. Indexes
# are considered starting from 1.
def shufleArray(a, n):
    n = n // 2

    start = n + 1
    j = n + 1
    for done in range(2 * n - 2):
        if (start == j):
            start -= 1
            j -= 1

        i = j - n if j > n else j
        j = 2 * i if j > n else 2 * i - 1

        a[start], a[j] = a[j], a[start]

    # Driver Code


if __name__ == "__main__":

    # The first element is bogus. We have used
    # one based indexing for simplicity.
    a = [-1, 1, 3, 5, 7, 2, 4, 6, 8]
    n = len(a)

    shufleArray(a, n)

    for i in range(1, n):
        print(a[i], end=" ")
