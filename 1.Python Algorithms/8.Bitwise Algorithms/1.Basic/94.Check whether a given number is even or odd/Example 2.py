# A Python3 code program
# to check for even or odd

# Returns true if n is even, else odd
def isEven(n):
    # n&1 is 1, then odd, else even
    return (not (n & 1))


# Driver code
n = 101
print("Even" if isEven(n) else "Odd")

# This code is contributed by "Sharad_Bhardwaj".
