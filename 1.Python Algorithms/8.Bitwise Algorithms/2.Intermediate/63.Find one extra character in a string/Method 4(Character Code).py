# Python Program to find extra character in one string
def findExtraCharacter(s1, s2):
    smallStr = ""
    largeStr = ""

    # Determine string with extra character
    if (len(s1) > len(s2)):
        smallStr = s2
        largeStr = s1
    else:
        smallStr = s1
        largeStr = s2
    smallStrCodeTotal = 0
    largeStrCodeTotal = 0
    i = 0

    # Add Character codes of both the strings
    while (i < len(smallStr)):
        smallStrCodeTotal += ord(smallStr[i])
        largeStrCodeTotal += ord(largeStr[i])
        i += 1

    # Add last character code of large string
    largeStrCodeTotal += ord(largeStr[i])

    # Minus the character code of smaller string
    # from the character code of large string
    # The result will be the extra character code
    intChar = largeStrCodeTotal - smallStrCodeTotal
    return chr(intChar)


# Driver code
s1 = "abcd"
s2 = "cbdae"
extraChar = findExtraCharacter(s1, s2)
print("Extra Character:", extraChar)

# This code is contributed by simranjenny84
