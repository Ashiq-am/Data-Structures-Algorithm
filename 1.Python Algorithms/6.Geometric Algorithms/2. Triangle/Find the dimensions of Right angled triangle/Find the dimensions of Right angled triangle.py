# Python code to find dimensions
# of Right angled triangle

# importing the math package
# to use sqrt function
from math import sqrt


# function to find the dimensions
def findDimen(H, A):
    # P ^ 2 + B ^ 2 = H ^ 2
    # P * B = 2 * A
    # (P + B)^2 = P ^ 2 + B ^ 2 + 2 * P*B = H ^ 2 + 4 * A
    # (P-B)^2 = P ^ 2 + B ^ 2-2 * P*B = H ^ 2-4 * A
    # P + B = sqrt(H ^ 2 + 4 * A)
    # |P-B| = sqrt(H ^ 2-4 * A)
    if H * H < 4 * A:
        print("Not Possible")
        return

    # sqrt value of H ^ 2 + 4A and H ^ 2- 4A
    apb = sqrt(H * H + 4 * A)
    asb = sqrt(H * H - 4 * A)

    # printing the dimensions
    print("P = ", "%.2f" % ((apb - asb) / 2.0))
    print("B = ", "%.2f" % ((apb + asb) / 2.0))


# driver code
H = 5  # assigning value to H
A = 6  # assigning value to A
findDimen(H, A)  # calliing function

# This code is contributed by "Abhishek Sharma 44"
