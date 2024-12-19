# Python3 program to schedule jobs so that
# each server gets an equal load.

# Function to find new array a
def solve(a, b, n):
    s = 0

    # find sum S of both arrays a and b.
    for i in range(0, n):
        s += a[i] + b[i]

    # Single element case.
    if n == 1:
        return a[0] + b[0]

    # This checks whether sum s can be divided
    # equally between all array elements. i.e.
    # whether all elements can take equal value
    # or not.
    if s % n != 0:
        return -1

    # Compute possible value of new
    # array elements.
    x = s // n

    for i in range(0, n):

        # Possibility 1
        if a[i] > x:
            return -1

        # ensuring that all elements of
        # array b are used.
        if i > 0:
            a[i] += b[i - 1]
            b[i - 1] = 0

        # If a(i) already updated to x
        # move to next element in array a.
        if a[i] == x:
            continue

        # Possibility 2
        y = a[i] + b[i]
        if i + 1 < n:
            y += b[i + 1]

        if y == x:
            a[i] = y
            b[i] = 0
            if i + 1 < n: b[i + 1] = 0
            continue

        # Possibility 3
        if a[i] + b[i] == x:
            a[i] += b[i]
            b[i] = 0
            continue

        # Possibility 4
        if i + 1 < n and a[i] + b[i + 1] == x:
            a[i] += b[i + 1]
            b[i + 1] = 0
            continue

        # If a(i) can not be made equal
        # to x even after adding all
        # possible elements from b(i)
        # then print -1.
        return -1

    # check whether all elements of b
    # are used.
    for i in range(0, n):
        if b[i] != 0:
            return -1

    # Return the new array element value.
    return x


# Driver Code
if __name__ == "__main__":
    a = [6, 14, 21, 1]
    b = [15, 7, 10, 10]
    n = len(a)
    print(solve(a, b, n))
