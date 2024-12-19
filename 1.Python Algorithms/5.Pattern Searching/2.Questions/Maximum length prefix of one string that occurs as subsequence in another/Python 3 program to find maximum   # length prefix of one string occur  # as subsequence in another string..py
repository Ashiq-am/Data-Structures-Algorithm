# Python 3 program to find maximum
# length prefix of one string occur
# as subsequence in another string.


# Return the maximum length
# prefix which is subsequence.
def maxPrefix(s, t):
    count = 0

    # Iterating string T.
    for i in range(0, len(t)):

        # If end of string S.
        if (count == len(s)):
            break

        # If character match,
        # increment counter.
        if (t[i] == s[count]):
            count = count + 1

    return count


# Driver Code
S = "digger"
T = "biggerdiagram"

print(maxPrefix(S, T))
