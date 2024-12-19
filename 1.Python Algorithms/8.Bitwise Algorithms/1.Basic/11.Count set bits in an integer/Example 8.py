# Check each bit in a number is set or not
# and return the total count of the set bits
def countSetBits(N):

    count = 0

    # (1 << i) = pow(2, i)
    for i in range(4*8):
        if(N & (1 << i)):
            count += 1
            return count

    # Driver code
    N = 15
    print(countSetBits(N))


    # This code is contributed by avanitrachhadiya2155
