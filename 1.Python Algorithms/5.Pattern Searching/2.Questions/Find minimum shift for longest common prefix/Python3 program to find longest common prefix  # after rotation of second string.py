# Python3 program to find longest common prefix
# after rotation of second string.

# function for KMP search
def KMP(m, n, str2, str1):
    pos = 0
    Len = 0

    # preprocessing of longest proper prefix
    p = [0 for i in range(m + 1)]
    k = 0

    for i in range(2, n + 1):
        while (k > 0 and str1[k] != str1[i - 1]):
            k = p[k]
        if (str1[k] == str1[i - 1]):
            k += 1
        p[i] = k

    # find out the longest prefix and position
    j = 0
    for i in range(m):
        while (j > 0 and j < n and str1[j] != str2[i]):
            j = p[j]
        if (j < n and str1[j] == str2[i]):
            j += 1

        # for new position with longer prefix
        # in str2 update pos and Len
        if (j > Len):
            Len = j
            pos = i - j + 1

    # prresult
    print("Shift = ", pos)
    print("Prefix = ", str1[:Len])


# Driver Code
str1 = "geeksforgeeks"
str2 = "forgeeksgeeks"
n = len(str1)
str2 = str2 + str2
KMP(2 * n, n, str2, str1)
