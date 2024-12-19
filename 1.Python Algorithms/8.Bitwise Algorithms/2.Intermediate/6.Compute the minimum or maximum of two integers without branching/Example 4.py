# Python3 program for the above approach
def max(x, y):
    abs = absbit32(x, y)
    return (x + y + abs) // 2


def min(x, y):
    abs = absbit32(x, y)
    return (x + y - abs) // 2


def absbit32(x, y):
    sub = x - y
    mask = (sub >> 31)
    return (sub ^ mask) - mask

# Driver code
print(max(2, 3))  # 3
print(max(2, -3))  # 2
print(max(-2, -3))  # -2
print(min(2, 3))  # 2
print(min(2, -3))  # -3
print(min(-2, -3))  # -3

# This code is contributed by rohitsingh07052.
