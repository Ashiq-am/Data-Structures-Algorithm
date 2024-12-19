def pow(a, b):
    if (b):
        return multiply(a, pow(a, b - 1))
    else:
        return 1

    # A recursive function to get x*y *


def multiply(x, y):
    if (y):
        return (x + multiply(x, y - 1))
    else:
        return 0

    # driver program to test above functions *


print(pow(5, 3))

# This code is contributed
# by Sam007
