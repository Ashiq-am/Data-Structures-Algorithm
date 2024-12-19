# Python3 program to check if a number
# is fibbinary number or not

# function to check whether a number
# is fibbinary or not
def isFibbinaryNum(n):
    # if the number does not contain adjacent
    # ones then (n & (n >> 1)) operation
    # results to 0
    if ((n & (n >> 1)) == 0):
        return 1

    # Not a fibbinary number
    return 0


# Driver code
n = 10

if (isFibbinaryNum(n)):
    print("Yes")
else:
    print("No")

# This code is contributed by sunnysingh
