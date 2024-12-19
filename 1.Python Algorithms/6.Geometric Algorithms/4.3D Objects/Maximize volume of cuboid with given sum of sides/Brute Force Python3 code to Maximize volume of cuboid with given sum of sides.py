# Python3 code to Maximize volume of
# cuboid with given sum of sides

# Return the maximum volume.
def maxvolume(s):
    maxvalue = 0

    # for length
    i = 1
    for i in range(s - 1):
        j = 1

        # for breadth
        for j in range(s):
            # for height
            k = s - i - j

            # calculating maximum volume.
            maxvalue = max(maxvalue, i * j * k)

    return maxvalue


# Driven Program
s = 8
print(maxvolume(s))

# This code is contributed by "Sharad_Bhardwaj".
