# Python3 program to check if given
# number is power of 4 or not

# Function to check if x is power of 4
def isPowerOfFour(n):
    count = 0

    # Check if there is only one
    # bit set in n
    if (n and (not (n & (n - 1)))):

        # count 0 bits before set bit
        while (n > 1):
            n >>= 1
            count += 1

        # If count is even then return
        # true else false
        if (count % 2 == 0):
            return True
        else:
            return False


# Driver code
test_no = 64
if (isPowerOfFour(64)):
    print(test_no, 'is a power of 4')
else:
    print(test_no, 'is not a power of 4')

# This code is contributed by Danish Raza
