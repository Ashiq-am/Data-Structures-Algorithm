# Python3 program to count total number of
# special sequences of length N where

# DP based function to find the number
# of special sequence
def getTotalNumberOfSequences(m, n):
    # define T and build in bottom manner to store
    # number of special sequences of length n and
    # maximum value m
    T = [[0 for i in range(n + 1)] for i in range(m + 1)]
    for i in range(m + 1):
        for j in range(n + 1):

            # Base case : If length of sequence is 0
            # or maximum value is 0, there cannot
            # exist any special sequence
            if i == 0 or j == 0:
                T[i][j] = 0

            # if length of sequence is more than
            # the maximum value, special sequence
            # cannot exist
            elif i < j:
                T[i][j] = 0

            # If length of sequence is 1 then the
            # number of special sequences is equal
            # to the maximum value
            # For example with maximum value 2 and
            # length 1, there can be 2 special
            # sequences {1}, {2}
            elif j == 1:
                T[i][j] = i
            else:
                T[i][j] = T[i - 1][j] + T[i // 2][j - 1]
    return T[m][n]


# Driver Code
if __name__ == '__main__':
    m = 10
    n = 4
    print('Total number of possible sequences ', getTotalNumberOfSequences(m, n))

# This code is contributed by sahilshelangia
