# Python3 program to find the largest
# sum zigzag sequence
MAX = 100


# Returns largest sum of a Zigzag
# sequence starting from (i, j) and
# ending at a bottom cell.
def largestZigZagSumRec(mat, i, j, n):
    # If we have reached bottom
    if (i == n - 1):
        return mat[i][j]

    # Find the largest sum by considering all
    # possible next elements in sequence.
    zzs = 0
    for k in range(n):
        if (k != j):
            zzs = max(zzs, largestZigZagSumRec(mat, i + 1, k, n))

    return zzs + mat[i][j]


# Returns largest possible sum of a
# Zizag sequence starting from top
# and ending at bottom.
def largestZigZag(mat, n):
    # Consider all cells of top row as
    # starting point
    res = 0
    for j in range(n):
        res = max(res, largestZigZagSumRec(mat, 0, j, n))

    return res


# Driver Code
if __name__ == "__main__":
    n = 3
    mat = [[4, 2, 1],
           [3, 9, 6],
           [11, 3, 15]]
    print("Largest zigzag sum: ",largestZigZag(mat, n))
