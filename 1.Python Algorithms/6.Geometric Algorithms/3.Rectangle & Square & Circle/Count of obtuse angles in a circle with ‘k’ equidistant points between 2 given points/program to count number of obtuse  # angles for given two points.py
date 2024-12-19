# C++ program to count number of obtuse
# angles for given two points.

def countObtuseAngles(a, b, k):
    # There are two arcs connecting a
    # and b. Let us count points on
    # both arcs.
    c1 = (b - a) - 1
    c2 = (k - b) + (a - 1)

    # Both arcs have same number of
    # points
    if (c1 == c2):
        return 0

    # Points on smaller arc is answer
    return min(c1, c2)


# Driver code
k, a, b = 6, 1, 3
print(countObtuseAngles(a, b, k))

# This code is contributed by Sachin Bisht
