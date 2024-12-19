# Python3 code to for marking multiples
import math


# index >> 5 corresponds to dividing index by 32
# index & 31 corresponds to modulo operation of
# index by 32

# Function to check value of bit position whether
# it is zero or one
def checkbit(array, index):
    return array[index >> 5] & (1 << (index & 31))


# Sets value of bit for corresponding index
def setbit(array, index):
    array[index >> 5] |= (1 << (index & 31))


# Driver code
a = 2
b = 10
size = abs(b - a)

# Size that will be used is actual_size/32
# ceil is used to initialize the array with
# positive number
size = math.ceil(size / 32)

# Array is dynamically initialized as
# we are calculating size at run time
array = [0 for i in range(size)]

# Iterate through every index from a to b and
# call setbit() if it is a multiple of 2 or 5
for i in range(a, b + 1):
    if (i % 2 == 0 or i % 5 == 0):
        setbit(array, i - a)

print("MULTIPLES of 2 and 5:")
for i in range(a, b + 1):
    if (checkbit(array, i - a)):
        print(i, end=" ")

# This code is contributed by rohitsingh07052
