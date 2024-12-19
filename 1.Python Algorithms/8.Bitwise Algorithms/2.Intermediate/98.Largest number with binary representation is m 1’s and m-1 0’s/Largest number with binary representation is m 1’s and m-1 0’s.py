# Python3 program to find
# largest number smaller
# than equal to n with m
# set bits then m-1 0 bits.
import math


# Returns largest number
# with m set bits then
# m-1 0 bits.
def answer(n):
    # Start with 2 bits.
    m = 2;

    # initial answer is
    # 1 which meets the
    # given condition
    ans = 1;
    r = 1;

    # check for all numbers
    while r < n:

        # compute the number
        r = (int)((pow(2, m) - 1) *
                  (pow(2, m - 1)));

        # if less than N
        if r < n:
            ans = r;

        # increment m to get
        # the next number
        m = m + 1;
    return ans;


# Driver Code
print(answer(7));

# This code is contributed by mits.
