# python 3 program to find profession of a person at
# given level and position.

# Returns 'e' if profession of node at given level
# and position is engineer. Else doctor. The function
# assumes that given position and level have valid values.
def findProffesion(level, pos):
    # Base case
    if (level == 1):
        return 'e'

    # Recursively find parent's profession. If parent
    # is a Doctor, this node will be a Doctor if it is
    # at odd position and an engineer if at even position
    if (findProffesion(level - 1, (pos + 1) // 2) == 'd'):
        if (pos % 2):
            return 'd'
        else:
            return 'e'

    # If parent is an engineer, then current node will be
    # an engineer if at add position and doctor if even
    # position.
    if (pos % 2):
        return 'e'
    else:
        return 'd'


# Driver code
if __name__ == '__main__':
    level = 3
    pos = 4
    if (findProffesion(level, pos) == 'e'):
        print("Engineer")
    else:
        print("Doctor")

# This code is contributed by
# Surendra_Gangwar
