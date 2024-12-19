# Efficiently check First repeated character
# in Python

# Returns -1 if all characters of str are
# unique.
# Assumptions : (1) str contains only characters
#				 from 'a' to 'z'
##			 (2) integers are stored using 32
##				 bits
def FirstRepeated(string):
    # An integer to store presence/absence
    # of 26 characters using its 32 bits.
    checker = 0

    pos = 0
    for i in string:
        val = ord(i) - ord('a');

        # If bit corresponding to current
        # character is already set
        if ((checker & (1 << val)) > 0):
            return pos

        # set bit in checker
        checker |= (1 << val)
        pos += 1

    return -1


# Driver code
string = "abcfdeacf"
i = FirstRepeated(string)
if i != -1:
    print("Char = ", string[i], " and Index = ", i)
else:
    print("No repeated Char")

# This code is contributed by Sachin Bisht
