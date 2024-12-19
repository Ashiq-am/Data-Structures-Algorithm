# Python 3 program to check if a number is
# Odious Number or not

# Function to get no of set bits in binary
# representation of passed binary no.
# Please refer below for details of this function :
# https://www.geeksforgeeks.org/count-set-bits-in-an-integer
def countSetBits(n):
    count = 0

    while (n):
        n = n & (n - 1)
        count = count + 1

    return count


# Check if number is odious or not
def checkOdious(n):
    return (countSetBits(n) % 2 == 1)


# Driver Code
num = 32

if (checkOdious(num)):
    print("Yes")
else:
    print("No")

# This code is contributed by Nikita Tiwari.
