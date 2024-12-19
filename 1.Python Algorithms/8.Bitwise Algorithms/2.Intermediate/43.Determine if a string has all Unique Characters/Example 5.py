# Python3 program to implement the approach
from collections import Counter


def uniqueCharacters(s):
    # If at any character more than once create another stream
    # stream count more than 0, return false
    return not any(filter(lambda x: x > 1, list(Counter(list(s)).values())))


# Driver code
input = "GeeksforGeeks"

if uniqueCharacters(input):
    print("The String " + input + " has all unique characters")

else:
    print("The String " + input + " has duplicate characters")

# This code is contributed by phasing17
