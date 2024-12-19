# Python3 program to check if two numbers
# are equal without using arithmetic
# and comparison operators

def areSame(a, b):
    # Function to check if two
    # numbers are equal using
    # XOR operator
    if ((a ^ b) != 0):
        print("Not Same")

    else:
        print("Same")

# Driver Code

areSame(10, 20)

# This code is contributed by Smitha
