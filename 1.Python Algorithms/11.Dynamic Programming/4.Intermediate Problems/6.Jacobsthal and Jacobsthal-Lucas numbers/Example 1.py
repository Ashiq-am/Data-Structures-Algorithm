# A simple Python3 recursive solution to
# find Jacobsthal and Jacobsthal-Lucas
# numbers

# Return nth Jacobsthal number.
def Jacobsthal(n):
    # base case
    if (n == 0):
        return 0

    # base case
    if (n == 1):
        return 1

    # recursive step.
    return Jacobsthal(n - 1) + 2 * Jacobsthal(n - 2)


# Return nth Jacobsthal-Lucas number.
def Jacobsthal_Lucas(n):
    # base case
    if (n == 0):
        return 2

    # base case
    if (n == 1):
        return 1

    # recursive step.
    return Jacobsthal_Lucas(n - 1) + 2 * Jacobsthal_Lucas(n - 2)


# Driven Program
n = 5
print("Jacobsthal number:", Jacobsthal(n))
print("Jacobsthal-Lucas number:", Jacobsthal_Lucas(n))
