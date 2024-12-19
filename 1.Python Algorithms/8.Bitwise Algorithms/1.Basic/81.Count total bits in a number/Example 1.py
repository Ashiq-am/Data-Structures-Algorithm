# Python3 program to find
# total bit in given number
import math


def countBits(number):
    # log function in base 2
    # take only integer part
    return int((math.log(number) /
                math.log(2)) + 1);


# Driver Code
num = 65;
print(countBits(num));

# This code is contributed by mits
