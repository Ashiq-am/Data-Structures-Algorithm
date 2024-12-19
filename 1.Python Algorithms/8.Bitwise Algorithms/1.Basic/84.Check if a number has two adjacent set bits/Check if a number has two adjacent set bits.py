# Python 3 program to check if there
# are two adjacent set bits.

def adjacentSet(n):
    return (n & (n >> 1))


# Driver Code
if __name__ == '__main__':
    n = 3
    if (adjacentSet(n)):
        print("Yes")
    else:
        print("No")

# This code is contributed by
# Shashank_Sharma
