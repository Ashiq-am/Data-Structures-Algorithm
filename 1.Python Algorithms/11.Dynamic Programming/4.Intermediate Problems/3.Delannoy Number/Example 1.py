# Python3 Program for finding
# nth Delannoy Number.

# Return the nth Delannoy Number.
def dealnnoy(n, m):
    # Base case
    if (m == 0 or n == 0):
        return 1

    # Recursive step.
    return dealnnoy(m - 1, n) + dealnnoy(m - 1, n - 1) + dealnnoy(m, n - 1)


# Driven code
n = 3
m = 4
print(dealnnoy(n, m))


