# python implementation to check
# whether the bit at given
# position is set or unset
# by Using left shift operator

import math


# function to check whether the bit
# at given position is set or unset
# by Using left shift operator
def bitAtGivenPosSetOrUnset(n, k):
    New_num = 1 << (k - 1)

    # returning result
    return (New_num & n)


# Driver code
n = 10
k = 2
if (bitAtGivenPosSetOrUnset(n, k)):
    print("Set")
else:
    print("Unset")

# This code is contributed by sam snehil
