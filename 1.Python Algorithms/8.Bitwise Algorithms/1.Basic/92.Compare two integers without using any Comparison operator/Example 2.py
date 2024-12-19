# Python3 program to compare two integers
# without any comparison operator.

# Function return 0 if
# A - B != 0 else return 1
def EqualNumber(A, B):


    diff = A - B
    if(diff):
        return 0
    else:
        return 1

# Driver Code
A = 5; B = 6
print((EqualNumber(A, B)))

# This code is contributed by kothavvsaakash
