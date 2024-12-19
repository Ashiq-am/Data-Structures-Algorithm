# Python3 program to count number
# of 2 x 2 squares in a right
# isosceles triangle
def numberOfSquares(base):
    # removing the extra part we would
    # always need
    base = (base - 2)

    # Since each square has base of
    # length of 2
    base = base // 2

    return base * (base + 1) / 2


# Driver code
base = 8

print(numberOfSquares(base))

# This code is contributed by Anant Agarwal and improved by heroichitesh.
