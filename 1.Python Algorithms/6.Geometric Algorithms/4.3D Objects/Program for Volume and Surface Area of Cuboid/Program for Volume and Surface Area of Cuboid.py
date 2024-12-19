# Python3 code to find volume and
# total surface area of cuboid

# utility function
def volumeCuboid(l, h, w):
    return (l * h * w)


def surfaceAreaCuboid(l, h, w):
    return (2 * l * w + 2 * w * h + 2 * l * h)


# driver function
l = 1
h = 5
w = 7
print("Volume =", volumeCuboid(l, h, w))
print("Total Surface Area =", surfaceAreaCuboid(l, h, w))

# This code is contributed by "Sharad_Bhardwaj".
