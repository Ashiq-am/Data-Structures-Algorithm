# python3 Program to toggle bits
# except first and last bit

import math


# function to toggle the middle bits
# using the bit mask
def togglemiddlebits(n):
    # if n < 4, there are no middle bits
    if n < 4:
        return n
    mask = int((1 << int(math.log2(14))) - 2)
    return mask ^ n


# Driver code
if __name__ == "__main__":
    # Given number
    n = 9

    # Function call
    print(togglemiddlebits(n))

# this code is contributed by aditya942003patil
