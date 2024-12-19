# Python3 program for the above approach

# Function to find binomial
# coefficient
def binomialCoeff(n, r):
    if (r > n):
        return 0

    m = 1000000007
    inv = [0 for i in range(r + 1)]
    inv[0] = 1;
    if (r + 1 >= 2)
        inv[1] = 1;

    # Getting the modular inversion
    # for all the numbers
    # from 2 to r with respect to m
    # here m = 1000000007
    for i in range(2, r + 1):
        inv[i] = m - (m // i) * inv[m % i] % m

    ans = 1

    # for 1/(r!) part
    for i in range(2, r + 1):
        ans = ((ans % m) * (inv[i] % m)) % m

    # for (n)*(n-1)*(n-2)*...*(n-r+1) part
    for i in range(n, n - r, -1):
        ans = ((ans % m) * (i % m)) % m

    return ans


# Driver code
n = 5
r = 2

print("Value of C(", n, ", ", r,
      ") is ", binomialCoeff(n, r))

