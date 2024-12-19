# Python3 program to count numbers whose
# bitwise OR and sum with N are equal

# Function to find total 0 bit in a number
def CountZeroBit(n):
    count = 0
    while (n):

        if (not (n & 1)):
            count += 1
        n >>= 1

    return count


# Function to find Count of non-negative
# numbers less than or equal to N, whose
# bitwise OR and SUM with N are equal.
def CountORandSumEqual(N):
    # count number of zero bit in N
    count = CountZeroBit(N)

    # power of 2 to count
    return (1 << count)


# Driver code
N = 10
print(CountORandSumEqual(N))

# This code is contributed by Anant Agarwal.
