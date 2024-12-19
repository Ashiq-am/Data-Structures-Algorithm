# Python program to count number of straight lines
# with n total points, out of which m are
# collinear.

# Returns value of binomial coefficient
# Code taken from https://goo.gl/vhy4jp
def nCk(n, k):
    C = [0] * (k + 1)

    C[0] = 1  # nC0 is 1

    for i in range(1, n + 1):

        # Compute next row of pascal triangle
        # using the previous row
        j = min(i, k)

        while (j > 0):
            C[j] = C[j] + C[j - 1]
            j = j - 1

    return C[k]


# function to calculate number of straight lines
# can be formed
def count_Straightlines(n, m):
    return (nCk(n, 2) - nCk(m, 2) + 1)


# Driven code
n = 4
m = 3
print(count_Straightlines(n, m))

# This code is contributed by "rishabh_jain".
