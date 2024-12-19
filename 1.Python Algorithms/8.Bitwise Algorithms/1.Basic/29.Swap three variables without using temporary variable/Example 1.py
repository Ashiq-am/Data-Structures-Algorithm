# python 3 program to swap three variables
# without using temporary variable.

# Assign c's value to a, a's value to b and
# b's value to c.
def swapThree(a, b, c):
    # Store sum of all in a
    a = a + b + c  # (a = 60)

    # After this, b has value of a
    b = a - (b + c)  # (b = 60 – (20+30) =10)

    # After this, c has value of b
    c = a - (b + c)  # (c = 60 – (10 + 30) = 20)

    # After this, a has value of c
    a = a - (b + c)  # (a = 60 – (10 + 20) = 30)

    print("After swapping a =", a, ", b =", b, ", c =", c)


# Driver code
if __name__ == '__main__':
    a = 10
    b = 20
    c = 30

    print("Before swapping a =", a, ", b =", b, ", c =", c)

    swapThree(a, b, c)

# This code is contributed by
# Surendra_Gangwar
