# Python3 program to implement
# wildcard pattern matching
# algorithm

# Function that matches input
# txt with given wildcard pattern
def stringmatch(txt, pat, n, m):
    # empty pattern can only
    # match with empty sting
    # Base case
    if (m == 0):
        return (n == 0)

    # step 1
    # initailze markers :
    i = 0
    j = 0
    index_txt = -1
    index_pat = -1
    while (i < n - 2):

        # For step - (2, 5)
        if (j < m and txt[i] == pat[j]):
            i += 1
            j += 1

        # For step - (3)
        elif (j < m and pat[j] == '?'):
            i += 1
            j += 1

        # For step - (4)
        elif (j < m and pat[j] == '*'):
            index_txt = i
            index_pat = j
            j += 1

        # For step - (5)
        elif (index_pat != -1):
            j = index_pat + 1
            i = index_txt + 1
            index_txt += 1

        # For step - (6)
        else:
            return False
    # For step - (7)
    while (j < m and pat[j] == '*'):
        j += 1

    # Final Check
    if (j == m):
        return True

    return False


# Driver code
strr = "baaabab"
pattern = "*****ba*****ab"

# char pattern[] = "ba*****ab"
# char pattern[] = "ba*ab"
# char pattern[] = "a*ab"
if (stringmatch(strr, pattern, len(strr),
                len(pattern))):
    print("Yes")
else:
    print("No")

pattern2 = "a*****ab"
if (stringmatch(strr, pattern2, len(strr),
                len(pattern2))):
    print("Yes")
else:
    print("No")
