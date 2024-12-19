# Python3 program to find maximum binary
# sub-matrix with row swaps and column swaps.
R, C = 5, 3


# Precompute the number of consecutive 1
# below the (i, j) in j-th column and the
# number of consecutive 1s on right side
# of (i, j) in i-th row.
def precompute(mat, ryt, dwn):
    # Travesing the 2d matrix from top-right.
    for j in range(C - 1, -1, -1):

        for i in range(0, R):

            # If (i,j) contain 0, do nothing
            if mat[i][j] == 0:
                ryt[i][j] = 0

            # Counting consecutive 1 on right side
            else:
                ryt[i][j] = ryt[i][j + 1] + 1

    # Travesing the 2d matrix from bottom-left.
    for i in range(R - 1, -1, -1):

        for j in range(0, C):

            # If (i,j) contain 0, do nothing
            if mat[i][j] == 0:
                dwn[i][j] = 0

            # Counting consecutive 1 down to (i,j).
            else:
                dwn[i][j] = dwn[i + 1][j] + 1


# Return maximum size submatrix
# with row swap allowed.
def solveRowSwap(ryt):
    b = [0] * R
    ans = 0

    for j in range(0, C):

        # Copying the column
        for i in range(0, R):
            b[i] = ryt[i][j]

        # Sort the copied array
        b.sort()

        # Find maximum submatrix size.
        for i in range(0, R):
            ans = max(ans, b[i] * (R - i))

    return ans


# Return maximum size submatrix
# with column swap allowed.
def solveColumnSwap(dwn):
    b = [0] * C
    ans = 0

    for i in range(0, R):

        # Copying the row.
        for j in range(0, C):
            b[j] = dwn[i][j]

        # Sort the copied array
        b.sort()

        # Find maximum submatrix size.
        for i in range(0, C):
            ans = max(ans, b[i] * (C - i))

    return ans


def findMax1s(mat):
    ryt = [[0 for i in range(C + 2)]
           for j in range(R + 2)]
    dwn = [[0 for i in range(C + 2)]
           for j in range(R + 2)]

    precompute(mat, ryt, dwn)

    # Solving for row swap and column swap
    rswap = solveRowSwap(ryt)
    cswap = solveColumnSwap(dwn)

    # Comparing both.
    if rswap > cswap:
        print("Row Swap\n", rswap)
    else:
        print("Column Swap\n", cswap)


# Driver Code
if __name__ == "__main__":
    mat = [[0, 0, 0],
           [1, 1, 0],
           [1, 1, 0],
           [0, 0, 0],
           [1, 1, 0]]

    findMax1s(mat)
