# Python3 program to illustrate String with unique
# characters without using any data structure
import math


def uniqueCharacters(string):
    # Assuming string can have characters
    # a-z this has 32 bits set to 0
    checker = 0

    for i in range(len(string)):
        bitAtIndex = ord(string[i]) - ord('a')

        # If that bit is already set in
        # checker, return False
        if ((bitAtIndex) > 0):
            if ((checker & ((1 << bitAtIndex))) > 0):
                return False

            # Otherwise update and continue by
            # setting that bit in the checker
            checker = checker | (1 << bitAtIndex)

    # No duplicates encountered, return True
    return True


# Driver Code
if __name__ == '__main__':

    input = "geekforgeeks"

    if (uniqueCharacters(input)):
        print("The String " + input +
              " has all unique characters")
    else:
        print("The String " + input +
              " has duplicate characters")

# This code is contributed by Princi Singh
