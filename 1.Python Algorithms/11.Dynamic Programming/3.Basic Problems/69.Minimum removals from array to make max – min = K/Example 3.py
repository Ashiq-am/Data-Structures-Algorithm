# Python3 program for the above approach

# To sort the array and return the answer
def removals(arr, n, k):



    # sort the array
    arr.sort()
    dp = [0 for i in range(n)]

    # Fill all stated with -1
    # when only one element
    for i in range(n):
        dp[i] = -1

    # As dp[0] = 0 (base case) so min
    # no of elements to be removed are
    # n-1 elements
    ans = n - 1
    dp[0] = 0



    for i in range(1, n):
        dp[i] = i
        j = dp[i - 1]


        while (j != i and arr[i] - arr[j] > k):
            j += 1


        dp[i] = min(dp[i], j)
        ans = min(ans, (n - (i - j + 1)))


    return ans

# Driver code
a = [1, 3, 4, 9, 10, 11, 12, 17, 20]
n = len(a)
k = 4

print(removals(a, n, k))
