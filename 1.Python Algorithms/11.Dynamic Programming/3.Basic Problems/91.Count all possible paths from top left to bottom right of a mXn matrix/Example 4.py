# Python3 program to count all possible
# paths from top left to top bottom
# using combinatorics
def numberOfPaths(m, n):
    # We have to calculate m + n-2 C n-1 here
    # which will be (m + n-2)! / (n-1)! (m-1)! path = 1;
    for i in range(n, (m + n - 1)):
        path *= i
        path //= (i - n + 1)

    return path


# Driver code
print(numberOfPaths(3, 3))
