# Python3 code to form binary palindrome

# function to apply DFS
def dfs(parent, ans, connectchars):
    # set the parent marked
    ans[parent] = 1

    # if the node has not been visited
    # set it and its children marked
    for i in range(len(connectchars[parent])):
        if (not ans[connectchars[parent][i]]):
            dfs(connectchars[parent][i], ans,
                connectchars)


def printBinaryPalindrome(n, k):
    arr = [0] * n
    ans = [0] * n

    # link which digits must be equal
    connectchars = [[] for i in range(k)]

    for i in range(n):
        arr[i] = i % k

    # connect the two indices
    for i in range(int(n / 2)):
        connectchars[arr[i]].append(arr[n - i - 1])
        connectchars[arr[n - i - 1]].append(arr[i])

    # set everything connected to
    # first character as 1
    dfs(0, ans, connectchars)

    for i in range(n):
        print(ans[arr[i]], end="")


# Driver Code
if __name__ == '__main__':
    n = 10
    k = 4
    printBinaryPalindrome(n, k)
