# Python3 program to find maximum sum in a grid such that
# no two elements are adjacent.

# Function to find max sum without adjacent
def maxSum(grid, n):
    # Sum including maximum element of first column
    incl = max(grid[0][0], grid[1][0])

    # Not including first column's element
    excl = 0

    # Traverse for further elements
    for i in range(1, n):
        # Update max_sum on including or excluding
        # of previous column
        excl_new = max(excl, incl)

        # Include current column. Add maximum element
        # from both row of current column
        incl = excl + max(grid[0][i], grid[1][i])

        # If current column doesn't to be included
        excl = excl_new

    # Return maximum of excl and incl
    # As that will be the maximum sum
    return max(excl, incl)


# Driver code
if __name__ == "__main__":
    grid = [[1, 2, 3, 4, 5],
            [6, 7, 8, 9, 10]]
    n = 5
    print(maxSum(grid, n))


