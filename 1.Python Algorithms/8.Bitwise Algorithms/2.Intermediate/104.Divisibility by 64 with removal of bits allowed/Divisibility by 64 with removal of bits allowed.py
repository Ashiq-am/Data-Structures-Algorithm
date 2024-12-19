# Python 3 program to find if given binary
# string can become divisible by 64 after
# removing some bits.

# function to check if it is possible
# to make it a multiple of 64.
def checking(s):
    c = 0

    # counter to count 0's
    n = len(s)

    # length of the string

    # loop which traverses right to left and
    # calculates the number of zeros before 1.
    i = n - 1
    while (i >= 0):
        if (s[i] == '0'):
            c += 1

        if (c >= 6 and s[i] == '1'):
            return True

        i -= 1

    return False


# Driver code
if __name__ == '__main__':
    s = "100010001"
    if (checking(s)):
        print("Possible")
    else:
        print("Not possible")

# This code is contributed by
# Surendra_Gangwar
