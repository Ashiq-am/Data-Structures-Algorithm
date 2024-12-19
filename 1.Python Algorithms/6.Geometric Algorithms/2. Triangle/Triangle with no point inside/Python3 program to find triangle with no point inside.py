# Python3 program to find triangle
# with no point inside
import sys


# method to get square of distance between
# (x1, y1) and (x2, y2)
def getDistance(x1, y1, x2, y2):
    return (x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1)


# Method prints points which make triangle
# with no point inside
def triangleWithNoPointInside(points, N):
    # any point can be chosen as
    # first point of triangle
    first = 0
    second = 0
    third = 0
    minD = sys.maxsize

    # choose nearest point as
    # second point of triangle
    for i in range(0, N):
        if i == first:
            continue

        # Get distance from first point and choose
        # nearest one
        d = getDistance(points[i][0], points[i][1],
                        points[first][0],
                        points[first][1])
        if minD > d:
            minD = d
            second = i

        # Pick third point by finding the second closest
    # point with different slope.
    minD = sys.maxsize
    for i in range(0, N):

        # if already chosen point then skip them
        if i == first or i == second:
            continue

        # get distance from first point
        d = getDistance(points[i][0], points[i][1],
                        points[first][0],
                        points[first][1])

        """ the slope of the third point with the first 
            point should not be equal to the slope of 
            second point with first point (otherwise 
            they'll be collinear) and among all such 
            points, we choose point with the smallest 
            distance """

        # here cross multiplication is compared instead
        # of division comparison
        if ((points[i][0] - points[first][0]) *
                (points[second][1] - points[first][1]) !=
                (points[second][0] - points[first][0]) *
                (points[i][1] - points[first][1])
                and minD > d):
            minD = d
            third = i

    print(points[first][0], ', ', points[first][1])
    print(points[second][0], ', ', points[second][1])
    print(points[third][0], ', ', points[third][1])


# Driver code
points = [[0, 0], [0, 2],
          [2, 0], [2, 2], [1, 1]]
N = len(points)
triangleWithNoPointInside(points, N)

# This code is contributed by Gowtham Yuvaraj
