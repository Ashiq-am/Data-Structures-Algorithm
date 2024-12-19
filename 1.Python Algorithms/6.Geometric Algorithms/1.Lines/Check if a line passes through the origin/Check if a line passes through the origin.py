# Python program to find if line
# passing through two coordinates
# also passes through origin or not

def checkOrigin(x1, y1, x2, y2):
    return (x1 * (y2 - y1) == y1 * (x2 - x1))


# Driver code
if (checkOrigin(1, 28, 2, 56) == True):
    print("Yes")
else:
    print("No")

# This code is contributed
# by Anant Agarwal.
