# A space efficient Python3 program to check if
# all characters of string are unique

# Returns true if all characters of str are
# unique.
# Assumptions : (1) str contains only characters
#				 from 'a' to 'z'
#			 (2) integers are stored using 32
#				 bits

def areCharactersUnique(s):
    # An integer to store presence/absence
    # of 26 characters using its 32 bits
    checker = 0

    for i in range(len(s)):

        val = ord(s[i]) - ord('a')

        # If bit corresponding to current
        # character is already set
        if (checker & (1 << val)) > 0:
            return False

        # set bit in checker
        checker |= (1 << val)

    return True


# Driver code
s = "aaabbccdaa"
if areCharactersUnique(s):
    print("Yes")
else:
    print("No")

# This code is contributed
# by Mohit Kumar
