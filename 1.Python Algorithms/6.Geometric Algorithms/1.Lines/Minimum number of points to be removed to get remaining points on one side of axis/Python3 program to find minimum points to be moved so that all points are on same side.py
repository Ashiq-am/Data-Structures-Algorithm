# Python3 program to find minimum points to be
# moved so that all points are on same side.

# Function to find the minimum number
# of points
def findmin(p, n):
    a, b, c, d = 0, 0, 0, 0
    for i in range(n):

        # Number of points on the left
        # of Y-axis.
        if (p[i][0] <= 0):
            a += 1

        # Number of points on the right
        # of Y-axis.
        elif (p[i][0] >= 0):
            b += 1

        # Number of points above X-axis.
        if (p[i][1] >= 0):
            c += 1

        # Number of points below X-axis.
        elif (p[i][1] <= 0):
            d += 1

    return min([a, b, c, d])


# Driver Code
p = [[1, 1], [2, 2], [-1, -1], [-2, 2]]
n = len(p)
print(findmin(p, n))

# This code is contributed by Mohit Kumar
