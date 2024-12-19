# A Naive Recursive Python 3 program to
# find maximum number of coins
# that can be collected before hitting a dead end
R = 5
C = 5


# to check whether current cell is out of the grid or not
def isValid(i, j):
    return (i >= 0 and i < R and j >= 0 and j < C)


# dir = 0 for left, dir = 1 for facing right.
# This function returns
# number of maximum coins that can be collected
# starting from (i, j).
def maxCoinsRec(arr, i, j, dir):
    # If this is a invalid cell or if cell is a blocking cell
    if (isValid(i, j) == False or arr[i][j] == '#'):
        return 0

    # Check if this cell contains the coin 'C' or if its empty 'E'.
    if (arr[i][j] == 'C'):
        result = 1
    else:
        result = 0

    # Get the maximum of two cases when you are facing right in this cell
    if (dir == 1):
        # Direction is right
        return (result + max(maxCoinsRec(arr, i + 1, j, 0),
                             maxCoinsRec(arr, i, j + 1, 1)))

    # Direction is left
    # Get the maximum of two cases when you are facing left in this cell
    return (result + max(maxCoinsRec(arr, i + 1, j, 1),
                         maxCoinsRec(arr, i, j - 1, 0)))


# Driver program to test above function
if __name__ == '__main__':
    arr = [['E', 'C', 'C', 'C', 'C'],
           ['C', '#', 'C', '#', 'E'],
           ['#', 'C', 'C', '#', 'C'],
           ['C', 'E', 'E', 'C', 'E'],
           ['C', 'E', '#', 'C', 'E']]

    # As per the question initial cell is (0, 0) and direction is
    # right
    print("Maximum number of collected coins is ", maxCoinsRec(arr, 0, 0, 1))
