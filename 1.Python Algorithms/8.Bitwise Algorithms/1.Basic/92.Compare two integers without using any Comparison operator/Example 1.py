# Python3 program to compare two integers
# without any comparison operator.

# Function return true if
# A ^ B > 0 else false
def EqualNumber(A, B):

	return ( A ^ B )

# Driver Code
A = 5; B = 6
print(int(not(EqualNumber(A, B))))

# This code is contributed by Smitha Dinesh Semwal.
