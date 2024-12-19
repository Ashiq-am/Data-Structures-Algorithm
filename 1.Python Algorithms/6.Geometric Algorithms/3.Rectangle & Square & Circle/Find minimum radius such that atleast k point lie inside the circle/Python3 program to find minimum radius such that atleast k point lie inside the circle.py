# Python3 program to find minimum radius
# such that atleast k point lie inside
# the circle


# Return minumum distance required so
# that aleast k point lie inside the
# circle.
def minRadius(k, x, y, n):
    dis = [0] * n

    # Finding distance between of each
    # point from origin

    for i in range(0, n):
        dis[i] = x[i] * x[i] + y[i] * y[i]

    # Sorting the distance
    dis.sort()

    return dis[k - 1]


# Driver Program
k = 3
x = [1, -1, 1]
y = [1, -1, -1]
n = len(x)

print(minRadius(k, x, y, n))

# This code is contributed by
# Prasad Kshirsagar
