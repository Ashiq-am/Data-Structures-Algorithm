# Python3 Program to find the
# area of a circumscribed circle
PI = 3.14159265


def areacircumscribed(a):
    return (a * a * (PI / 2))


# Driver code
a = 6
print(" Area of an circumscribed circle is :",
      round(areacircumscribed(a), 2))

# This code is contributed by Smitha Dinesh Semwal
