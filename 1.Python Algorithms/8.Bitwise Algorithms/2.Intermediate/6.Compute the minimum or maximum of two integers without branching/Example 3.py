# Python3 implementation of the approach
import sys

CHAR_BIT = 8
INT_BIT = sys.getsizeof(int())


# Function to find minimum of x and y
def Min(x, y):
    return y + ((x - y) & ((x - y) >>
                           (INT_BIT * CHAR_BIT - 1)))


# Function to find maximum of x and y
def Max(x, y):
    return x - ((x - y) & ((x - y) >>
                           (INT_BIT * CHAR_BIT - 1)))


# Driver code
x = 15
y = 6
print("Minimum of", x, "and",
      y, "is", Min(x, y))
print("Maximum of", x, "and",
      y, "is", Max(x, y))

# This code is contributed by PrinciRaj1992
