# Python program for sub-optimal
# approach of SumOverSubsets DP

# function to print sum over subsets value
def SumOverSubsets(a, n):
    sos = [0] * (1 << n)

    # iterate for all possible x
    for x in range((1 << n)):
        sos[x] = a[0]

        # iterate for the bitwise subsets only
        i = x

        while i > 0:
            sos[x] += a[i]
        i = ((i - 1) & x)

    # prall the subsets
    for i in range(1 << n):
        print(sos[i], end=" ")


# Driver Code
if __name__ == '__main__':
    a = [7, 12, 14, 16]
    n = 2
    SumOverSubsets(a, n)
