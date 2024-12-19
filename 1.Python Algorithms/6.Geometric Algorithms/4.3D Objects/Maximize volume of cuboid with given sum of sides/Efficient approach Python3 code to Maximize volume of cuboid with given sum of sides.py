# Python3 code to Maximize volume of
# cuboid with given sum of sides

# Return the maximum volume.
def maxvolume(s):
    # finding length
    length = int(s / 3)

    s -= length

    # finding breadth
    breadth = s / 2

    # finding height
    height = s - breadth

    return int(length * breadth * height)


# Driven Program
s = 8
print(maxvolume(s))

# This code is contributed by "Sharad_Bhardwaj".
