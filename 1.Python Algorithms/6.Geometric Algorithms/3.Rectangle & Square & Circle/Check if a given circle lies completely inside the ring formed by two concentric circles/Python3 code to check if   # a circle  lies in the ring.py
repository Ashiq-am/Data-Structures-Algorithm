# Python3 code to check if
# a circle lies in the ring
import math


# Function to check if circle
# lies in the ring
def checkcircle(r, R, r1, x1, y1):
    # distance between center of circle
    # center of concentric circles(origin)
    # using Pythagoras theorem
    dis = int(math.sqrt(x1 * x1 + y1 * y1))

    # Condition to check if circle is
    # strictly inside the ring
    return (dis - r1 >= R and dis + r1 <= r)


# Driver Code

# Both circle with radius 'r'
# and 'R' have center (0,0)
r = 8
R = 4
r1 = 2
x1 = 6
y1 = 0
if (checkcircle(r, R, r1, x1, y1)):
    print("yes")
else:
    print("no")

# This code is contributed by Smitha Dinesh Semwal.
