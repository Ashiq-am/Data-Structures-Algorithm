# Python3 program to find maximum difference
# of sum of elements of two rows

# Function to find maximum difference of
# sum of elements of two rows such that
# second row appears before first row.
def maxRowDiff(mat, m, n):
    # auxiliary array to store sum of
    # all elements of each row
    rowSum = [0] * m

    # calculate sum of each row and
    # store it in rowSum array
    for i in range(0, m):
        sum = 0
        for j in range(0, n):
            sum += mat[i][j]
        rowSum[i] = sum

    # calculating maximum difference of
    # two elements such that
    # rowSum[i]<rowsum[j]
    max_diff = rowSum[1] - rowSum[0]
    min_element = rowSum[0]

    for i in range(1, m):

        # if current difference is greater
        # than previous then update it
        if (rowSum[i] - min_element > max_diff):
            max_diff = rowSum[i] - min_element

        # if new element is less than previous
        # minimum element then update it so
        # that we may get maximum difference
        # in remaining array
        if (rowSum[i] < min_element):
            min_element = rowSum[i]
    return max_diff


# Driver program to run the case
m = 5
n = 4
mat = [[-1, 2, 3, 4],
       [5, 3, -2, 1],
       [6, 7, 2, -3],
       [2, 9, 1, 4],
       [2, 1, -2, 0]]

print(maxRowDiff(mat, m, n))
