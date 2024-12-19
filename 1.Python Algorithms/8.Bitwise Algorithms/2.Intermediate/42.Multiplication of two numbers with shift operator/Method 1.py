# python 3 program to find multiplication
# of two number without use of
# multiplication operator

# Function for multiplication
def multiply(n, m):
    ans = 0
    count = 0
    while (m):
        # check for set bit and left
        # shift n, count times
        if (m % 2 == 1):
            ans += n << count

        # increment of place value (count)
        count += 1
        m = int(m / 2)

    return ans


# Driver code
if __name__ == '__main__':
    n = 20
    m = 13
    print(multiply(n, m))

# This code is contributed by
# Ssanjit_Prasad
