# Python3 program to find maximum decimal
# value path in binary matrix
N = 4


# Returns maximum decimal value in binary
# matrix. Here p indicate power of 2
def maxDecimalValue(mat, i, j, p):
    # Out of matrix boundary
    if i >= N or j >= N:
        return 0

    result = max(
        maxDecimalValue(mat, i, j + 1, p + 1),
        maxDecimalValue(mat, i + 1, j, p + 1))

    # If current matrix value is 1 then
    # return result + power(2, p) else
    # result
    if mat[i][j] == 1:
        return pow(2, p) + result
    else:
        return result


# Driver Program
mat = [[1, 1, 0, 1],
       [0, 1, 1, 0],
       [1, 0, 0, 1],
       [1, 0, 1, 1]]

print(maxDecimalValue(mat, 0, 0, 0))
