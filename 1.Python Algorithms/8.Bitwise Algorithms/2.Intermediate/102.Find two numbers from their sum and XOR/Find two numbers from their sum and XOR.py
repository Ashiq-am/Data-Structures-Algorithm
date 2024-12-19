# Python program to find two numbers with
# given Sum and XOR such that value of
# first number is minimum.


# Function that takes in the sum and XOR
# of two numbers and generates the two
# numbers such that the value of X is
# minimized
def compute(S, X):
    A = (S - X) // 2
    a = 0
    b = 0

    # Traverse through all bits
    for i in range(64):
        Xi = (X & (1 << i))
        Ai = (A & (1 << i))
        if (Xi == 0 and Ai == 0):
            # Let us leave bits as 0.
            pass

        elif (Xi == 0 and Ai > 0):
            a = ((1 << i) | a)
            b = ((1 << i) | b)

        elif (Xi > 0 and Ai == 0):
            a = ((1 << i) | a)
        # We leave i-th bit of b as 0.

        else:  # (Xi == 1 and Ai == 1)
            print("Not Possible")
            return

    print("a = ", a)
    print("b =", b)


# Driver function
S = 17
X = 13
compute(S, X)

# This code is contributed by ankush_953
