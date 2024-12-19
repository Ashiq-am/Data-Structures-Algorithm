# Python3 program to find maximum points
# that can be collected in a journey from
# top to bottom and then back from bottom to top,
MAX = 5
N = 5
M = 5
inf = 100000


# Calculating the points at a (row1, col1) and
# (row2, col2) from path1 and path2
def cost(grid, row1, col1, row2, col2):
    # If both path is at same cell
    if (row1 == row2 and col1 == col2):

        # If the cell contain *, return 1
        if (grid[row1][col1] == '*'):
            return 1

        # else return 0.
        return 0

    ans = 0

    # If path 1 contain *, add to answer.
    if (grid[row1][col1] == '*'):
        ans += 1

    # If path contain *, add to answer.
    if (grid[row2][col2] == '*'):
        ans += 1

    return ans


# Calculate the maximum points that can be
# collected.
def solve(n, m, grid, dp, row1, col1, row2):
    col2 = (row1 + col1) - (row2)

    # If both path reach the bottom right cell
    if (row1 == n - 1 and col1 == m - 1 and
            row2 == n - 1 and col2 == m - 1):
        return 0

    # If moving out of grid
    if (row1 >= n or col1 >= m or
            row2 >= n or col2 >= m):
        return -1 * inf

    # If already calculated, return the value
    if (dp[row1][col1][row2] != -1):
        return dp[row1][col1][row2]

    # Variable for 4 options.
    ch1 = -1 * inf
    ch2 = -1 * inf
    ch3 = -1 * inf
    ch4 = -1 * inf

    # If path 1 is moving right and path 2
    # is moving down.
    if (col1 + 1 < m and row2 + 1 < n and
            grid[row1][col1 + 1] != '#' and
            grid[row2 + 1][col2] != '#'):
        ch1 = cost(grid, row1, col1 + 1, row2 + 1, col2) + \
              solve(n, m, grid, dp, row1, col1 + 1, row2 + 1)

    # If path 1 is moving right and path 2
    # is moving right.
    if (col1 + 1 < m and col2 + 1 < m and
            grid[row1][col1 + 1] != '#' and
            grid[row2][col2 + 1] != '#'):
        ch2 = cost(grid, row1, col1 + 1, row2, col2 + 1) + \
              solve(n, m, grid, dp, row1, col1 + 1, row2)

    # If path 1 is moving down and path 2
    # is moving right.
    if (row1 + 1 < n and col2 + 1 < m and
            grid[row1 + 1][col1] != '#' and
            grid[row2][col2 + 1] != '#'):
        ch3 = cost(grid, row1 + 1, col1, row2, col2 + 1) + \
              solve(n, m, grid, dp, row1 + 1, col1, row2)

    # If path 1 is moving down and path 2 is moving down.
    if (row1 + 1 < n and row2 + 1 < n and
            grid[row1 + 1][col1] != '#' and
            grid[row2 + 1][col2] != '#'):
        ch4 = cost(grid, row1 + 1, col1, row2 + 1, col2) + \
              solve(n, m, grid, dp, row1 + 1, col1, row2 + 1)

    # Returning the maximum of 4 options.
    dp[row1][col1][row2] = max(ch1, ch2, ch3, ch4)
    return dp[row1][col1][row2]


# Wrapper Function
def wrapper(n, m, grid):
    ans = 0

    dp = [[[-1] * MAX for i in range(MAX)]
          for j in range(MAX)]

    # If last bottom right cell is blcoked
    if (grid[n - 1][m - 1] == '#' or
            grid[0][0] == '#'):
        ans = -1 * inf

    # If top left cell contain *
    if (grid[0][0] == '*'):
        ans += 1
    grid[0][0] = '.'

    # If bottom right cell contain *
    if (grid[n - 1][m - 1] == '*'):
        ans += 1
    grid[n - 1][m - 1] = '.'

    ans += solve(n, m, grid, dp, 0, 0, 0)
    return max(ans, 0)


# Driver Code
if __name__ == '__main__':
    n = 5
    m = 5

    grid = [['.', '*', '.', '*', '.'],
            ['*', '#', '#', '#', '.'],
            ['*', '.', '*', '.', '*'],
            ['.', '#', '#', '#', '*'],
            ['.', '*', '.', '*', '.']]

    print(wrapper(n, m, grid))
