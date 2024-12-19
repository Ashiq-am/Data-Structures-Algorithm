# Python 3 program
# for brute force
# approach of SumOverSubsets DP

# function to print the
# sum over subsets value
def SumOverSubsets(a, n):
    # array to store
    # the SumOverSubsets
    sos = [0] * (1 << n)

    # iterate for all possible x
    for x in range(0, (1 << n)):

        # iterate for all
        # possible bitwise subsets
        for i in range(0, (1 << n)):

            # if i is a bitwise subset of x
            if ((x & i) == i):
                sos[x] += a[i]

    # printa all the subsets
    for i in range(0, (1 << n)):
        print(sos[i], end=" ")


# Driver Code
a = [7, 12, 14, 16]
n = 2
SumOverSubsets(a, n)
