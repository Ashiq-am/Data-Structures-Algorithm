# Python3 program to find count
# of values whose XOR with
# x is greater than x and
# values are smaller than x

def countValues(x):
    # Initialize result
    count = 0;
    n = 1;

    # Traversing through
    # all bits of x
    while (x > 0):

        # If current last bit
        # of x is set then
        # increment count by
        # n. Here n is a power
        # of 2 corresponding
        # to position of bit
        if (x % 2 == 0):
            count += n;

        # Simultaneously
        # calculate the 2^n
        n *= 2;

        # Replace x with x/2;
        x /= 2;
        x = int(x);

    return count;


# Driver code
x = 10;
print(countValues(x));

# This code is contributed
# by mits
