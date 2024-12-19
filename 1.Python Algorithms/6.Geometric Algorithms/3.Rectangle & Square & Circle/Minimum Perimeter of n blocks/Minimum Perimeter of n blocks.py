# Python3 program to find minimum
# perimeter using n blocks.
import math


def minPerimeter(n):
    l = math.sqrt(n)
    sq = l * l

    # if n is a perfect square
    if (sq == n):
        return l * 4
    else:
        # Number of rows
        row = n / l

        # perimeter of the
        # rectangular grid
        perimeter = 2 * (l + row)

        # if there are blocks left
        if (n % l != 0):
            perimeter += 2
        return perimeter

    # Driver code


n = 10
print(int(minPerimeter(n)))

# This code is contributed by
# Prasad Kshirsagar
