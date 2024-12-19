# Python Program to detect
# if two integers have opposite signs.

def oppositeSigns(x, y):
    product = x * y
    return (product < 0)


# driver code
x = 100
y = -100
if (oppositeSigns(x, y) == True):
    print("Signs are opposite")
else:
    print("Signs are not opposite")

# this code is contributed by shinjanpatra
