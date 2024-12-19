# Python3 program to find if there
# is path from top left to right bottom
row = 5
col = 5


# to find the path from
# top left to bottom right
def isPath(arr):
    # set arr[0][0] = 1
    arr[0][0] = 1

    # Mark reachable (from top left)
    # nodes in first row and first column.
    for i in range(1, row):
        if (arr[i][0] != -1):
            arr[i][0] = arr[i - 1][0]

    for j in range(1, col):
        if (arr[0][j] != -1):
            arr[0][j] = arr[0][j - 1]

    # Mark reachable nodes in
    # remaining matrix.
    for i in range(1, row):
        for j in range(1, col):
            if (arr[i][j] != -1):
                arr[i][j] = max(arr[i][j - 1],
                                arr[i - 1][j])

    # return yes if right
    # bottom index is 1
    return (arr[row - 1][col - 1] == 1)


# Driver Code

# Given array
arr = [[0, 0, 0, -1, 0],
       [-1, 0, 0, -1, -1],
       [0, 0, 0, -1, 0],
       [-1, 0, -1, 0, -1],
       [0, 0, -1, 0, 0]]

# path from arr[0][0] to arr[row][col]
if (isPath(arr)):
    print("Yes")
else:
    print("No")
