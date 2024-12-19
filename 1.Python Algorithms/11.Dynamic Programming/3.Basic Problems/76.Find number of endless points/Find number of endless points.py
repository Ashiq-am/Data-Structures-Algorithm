# Python3 program to find count of
# endless points
import numpy as np


# Returns count of endless points
def countEndless(input_mat, n):
    row = np.zeros((n, n))
    col = np.zeros((n, n))

    # Fills column matrix. For every column,
    # start from every last row and fill
    # every entry as blockage after a 0 is found.
    for j in range(n):

        # flag which will be zero once we
        # get a '0' and it will be 1 otherwise
        isEndless = 1

        for i in range(n - 1, -1, -1):

            # encountered a '0', set the
            # isEndless variable to false
            if (input_mat[i][j] == 0):
                isEndless = 0

            col[i][j] = isEndless

    # Similarly, fill row matrix
    for i in range(n):

        isEndless = 1
        for j in range(n - 1, -1, -1):

            if (input_mat[i][j] == 0):
                isEndless = 0

            row[i][j] = isEndless

    # Calculate total count of endless points
    ans = 0
    for i in range(n):
        for j in range(1, n):

            # If there is NO blockage in row
            # or column after this point,
            # increment result.
            # print(row[i][j] , col[i][j])
            if (row[i][j] and col[i][j]):
                ans += 1
        # print(ans)

    return ans


# Driver code
if __name__ == "__main__":
    input_mat = [[1, 0, 1, 1],
                 [0, 1, 1, 1],
                 [1, 1, 1, 1],
                 [0, 1, 1, 0]]
    n = 4

    print(countEndless(input_mat, n))
