# Python3 program to Multiplying a
# variable with a constant

# Returns n * 7
def multiplyBySeven(n):
    # OR (n << 2) + (n << 1) + n
    return (n << 3) - n


# Returns n * 12
def multiplyByTwelve(n):
    return (n << 3) + (n << 2)


# Driver code
print(multiplyBySeven(5))
print(multiplyByTwelve(5))

# This code is contributed by Anant Agarwal.
