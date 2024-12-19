# Python3 program to find whether a
# regular polygon is possible in circle
# with 1s as vertices
from math import sqrt


# method returns true if polygon is
# possible with 'midpoints' number
# of midpoints
def checkPolygonWithMidpoints(arr, N, midpoints):
    # loop for getting first vertex of polygon
    for j in range(midpoints):

        val = 1

        # loop over array values at
        # 'midpoints' distance
        for k in range(j, N, midpoints):
            # and(&) all those values, if even
            # one of them is 0, val will be 0
            val &= arr[k]

        # if val is still 1 and (N/midpoints) or (number
        # of vertices) are more than two (for a polygon
        # minimum) print result and return true
        if (val and N // midpoints > 2):
            print("Polygon possible with side length",
                  (N // midpoints))
            return True

    return False


# method prints sides in the polygon or print
# not possible in case of no possible polygon
def isPolygonPossible(arr, N):
    # limit for iterating over divisors
    limit = sqrt(N)
    for i in range(1, int(limit) + 1):

        # If i divides N then i and (N/i)
        # will be divisors
        if (N % i == 0):

            # check polygon for both divisors
            if (checkPolygonWithMidpoints(arr, N, i) or
                    checkPolygonWithMidpoints(arr, N, (N // i))):
                return

    print("Not possiblen")


# Driver code
if __name__ == "__main__":
    arr = [1, 0, 1, 0, 1, 0, 1, 0, 1, 1]
    N = len(arr)
    isPolygonPossible(arr, N)
