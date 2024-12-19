# Python3 program to find all
# Pandigital concatenations
# of two strings.

# Checks if a given
# is Pandigital
def isPanDigital(s):
    digits = [False] * 10

    for i in range(0, len(s)):
        digits[int(s[i]) -
               int('0')] = True

    # digit i is not present
    # thus not pandigital
    for i in range(0, 10):
        if (digits[i] == False):
            return False

    return True


# Returns number of pairs
# of strings resulting in
# Pandigital Concatenations
def countPandigitalPairs(v):
    # iterate over all
    # pair of strings
    pairs = 0
    for i in range(0, len(v)):

        for j in range(i + 1,
                       len(v)):

            if (isPanDigital(v[i] +
                             v[j])):
                pairs = pairs + 1
    return pairs


# Driver code
v = ["123567", "098234",
     "14765", "19804"]

print(countPandigitalPairs(v))
