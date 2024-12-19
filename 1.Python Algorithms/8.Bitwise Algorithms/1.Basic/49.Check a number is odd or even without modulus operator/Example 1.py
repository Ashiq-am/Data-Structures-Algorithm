# A simple Python program to
# check for even or odd

# Returns true if n is even,
# else odd
def isEven(n):
    isEven = True;
    for i in range(1, n + 1):
        if isEven == True:
            isEven = False;
        else:
            isEven = True;

    return isEven;


# Driver code
n = 101;
if isEven(n) == True:
    print("Even");
else:
    print("Odd");

# This code is contributed by
# Manish Shaw (manishshaw1)
