# Python3 code to find optimal way to break
# cuboid into cubes.
from fractions import gcd


# Print the maximum side and no of cube.
def maximizecube(l, b, h):
    # GCD to find side.
    side = gcd(l, gcd(b, h))

    # dividing to find number of cubes.
    num = int(l / side)
    num = int(num * b / side)
    num = int(num * h / side)

    print(side, num)


# Driver code
l = 2
b = 4
h = 6

maximizecube(l, b, h)
