# Python3 program to get minimum lines to cover
# all the points

# Utility method to get gcd of a and b
def gcd(a, b):
    if (b == 0):
        return a
    return gcd(b, a % b)


# method returns reduced form of dy/dx as a pair
def getReducedForm(dy, dx):
    g = gcd(abs(dy), abs(dx))

    # get sign of result
    sign = (dy < 0) ^ (dx < 0)

    if (sign):
        return (-abs(dy) // g, abs(dx) // g)
    else:
        return (abs(dy) // g, abs(dx) // g)

    # /* method returns minimum number of lines to


#	 cover all points where all lines goes
#	 through (xO, yO) */
def minLinesToCoverPoints(points, N, xO, yO):
    # set to store slope as a pair
    st = dict()
    minLines = 0

    # loop over all points once
    for i in range(N):

        # get x and y co-ordinate of current point
        curX = points[i][0]
        curY = points[i][1]

        temp = getReducedForm(curY - yO, curX - xO)

        # if this slope is not there in set,
        # increase ans by 1 and insert in set
        if (temp not in st):
            st[temp] = 1
            minLines += 1

    return minLines


# Driver code
xO = 1
yO = 0

points = [[-1, 3],
          [4, 3],
          [2, 1],
          [-1, -2],
          [3, -3]]

N = len(points)
print(minLinesToCoverPoints(points, N, xO, yO))

# This code is contributed by mohit kumar 29
