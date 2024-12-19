# Python3 program to find profession of a person at
# given level and position.

""" Function to get no of set bits in binary
representation of passed binary no. """


def countSetBits(n):
    count = 0
    while n > 0:
        n &= (n - 1)
    count += 1
    return count


# Returns 'e' if profession of node at given level
# and position is engineer. Else doctor. The function
# assumes that given position and level have valid values.
def findProffesion(level, pos):
    # Count set bits in 'pos-1'
    c = countSetBits(pos - 1)

    # If set bit count is odd, then doctor, else engineer
    if c % 2 == 0:
        return 'e'
    else:
        return 'd'


level, pos = 3, 4
if findProffesion(level, pos) == 'e':
    print("Engineer")
else:
    print("Doctor")

# This code is contributed by divyeshrabadiya07.
