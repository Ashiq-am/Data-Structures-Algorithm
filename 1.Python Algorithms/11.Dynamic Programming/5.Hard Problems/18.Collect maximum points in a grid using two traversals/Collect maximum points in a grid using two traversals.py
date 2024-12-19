# A Memoization based program to find maximum collection
# using two traversals of a grid

R = 5
C = 4
intmin = -10000000
intmax = 10000000


# checks whether a given input is valid or not
def isValid(x, y1, y2):
    return ((x >= 0 and x < R and y1 >= 0
             and y1 < C and y2 >= 0 and y2 < C))


# Driver function to collect max value
def getMaxUtil(arr, mem, x, y1, y2):
    # ---------- BASE CASES -----------
    if isValid(x, y1, y2) == False:
        return intmin

    # if both traversals reach their destinations
    if x == R - 1 and y1 == 0 and y2 == C - 1:
        if y1 == y2:
            return arr[x][y1]
        else:
            return arr[x][y1] + arr[x][y2]

    # If both traversals are at last row
    # but not at their destination
    if x == R - 1:
        return intmin

    # If subproblem is already solved
    if mem[x][y1][y2] != -1:
        return mem[x][y1][y2]

    # Initialize answer for this subproblem
    ans = intmin

    # this variable is used to store gain of current cell(s)
    temp = 0
    if y1 == y2:
        temp = arr[x][y1]
    else:
        temp = arr[x][y1] + arr[x][y2]

    # Recur for all possible cases, then store and return the
    # one with max value
    ans = max(ans, temp + getMaxUtil(arr, mem, x + 1, y1, y2 - 1))
    ans = max(ans, temp + getMaxUtil(arr, mem, x + 1, y1, y2 + 1))
    ans = max(ans, temp + getMaxUtil(arr, mem, x + 1, y1, y2))

    ans = max(ans, temp + getMaxUtil(arr, mem, x + 1, y1 - 1, y2))
    ans = max(ans, temp + getMaxUtil(arr, mem, x + 1, y1 - 1, y2 - 1))
    ans = max(ans, temp + getMaxUtil(arr, mem, x + 1, y1 - 1, y2 + 1))

    ans = max(ans, temp + getMaxUtil(arr, mem, x + 1, y1 + 1, y2))
    ans = max(ans, temp + getMaxUtil(arr, mem, x + 1, y1 + 1, y2 - 1))
    ans = max(ans, temp + getMaxUtil(arr, mem, x + 1, y1 + 1, y2 + 1))

    mem[x][y1][y2] = ans
    return ans


# This is mainly a wrapper over recursive
# function getMaxUtil().
# This function creates a table for memoization and calls
# getMaxUtil()

def geMaxCollection(arr):
    # Create a memoization table and
    # initialize all entries as -1
    mem = [[[-1 for i in range(C)] for i in range(C)] for i in range(R)]

    # Calculation maximum value using
    # memoization based function
    # getMaxUtil()
    return getMaxUtil(arr, mem, 0, 0, C - 1)


# Driver program to test above functions
if __name__ == '__main__':
    arr = [[3, 6, 8, 2],
           [5, 2, 4, 3],
           [1, 1, 20, 10],
           [1, 1, 20, 10],
           [1, 1, 20, 10],
           ]
    print('Maximum collection is ', geMaxCollection(arr))
