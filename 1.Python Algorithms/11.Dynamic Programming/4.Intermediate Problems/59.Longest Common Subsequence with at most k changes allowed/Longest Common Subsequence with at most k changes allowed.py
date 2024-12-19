# Python3 program to find LCS of two arrays
# with k changes allowed in the first array.
MAX = 10


# Return LCS with at most k changes allowed.
def lcs(dp, arr1, n, arr2, m, k):
    # If at most changes is less than 0.
    if k < 0:
        return -(10 ** 7)

    # If any of two array is over.
    if n < 0 or m < 0:
        return 0

    # Making a reference variable to dp[n][m][k]
    ans = dp[n][m][k]

    # If value is already calculated,
    # return that value.
    if ans != -1:
        return ans

    # calculating LCS with no changes made.
    ans = max(lcs(dp, arr1, n - 1, arr2, m, k),
              lcs(dp, arr1, n, arr2, m - 1, k))

    # calculating LCS when array element are same.
    if arr1[n - 1] == arr2[m - 1]:
        ans = max(ans, 1 + lcs(dp, arr1, n - 1,
                               arr2, m - 1, k))

    # calculating LCS with changes made.
    ans = max(ans, lcs(dp, arr1, n - 1,
                       arr2, m - 1, k - 1))

    return ans


# Driven Program
if __name__ == "__main__":
    k = 1
    arr1 = [1, 2, 3, 4, 5]
    arr2 = [5, 3, 1, 4, 2]
    n = len(arr1)
    m = len(arr2)

    dp = [[[-1 for i in range(MAX)] for j in range(MAX)] for k in range(MAX)]

    print(lcs(dp, arr1, n, arr2, m, k))
