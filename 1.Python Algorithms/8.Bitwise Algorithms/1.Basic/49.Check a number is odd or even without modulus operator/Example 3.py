# A simple Python program to
# check for even or odd
# Returns 0 if n
# is even, else odd
def isEven(n):
    # n&1 is 1, then
    # odd, else even
    return (n & 1);


# Driver code
n = 101;
if (isEven(n) == 0):
    print("Even");
else:
    print("Odd");

# This code is contributed
# by Manish Shaw (manishshaw1)
