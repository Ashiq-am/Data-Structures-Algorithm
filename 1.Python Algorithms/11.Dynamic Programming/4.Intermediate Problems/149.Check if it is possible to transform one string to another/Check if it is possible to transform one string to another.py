# Python3 program to check if a string can
# be converted to another string by
# performing operations


# function to check if a string can be
# converted to another string by
# performing following operations
def check(s1, s2):
    # calculates length
    n = len(s1)
    m = len(s2)
    dp = ([[False for i in range(m + 1)]
           for i in range(n + 1)])

    # mark 1st position as true
    dp[0][0] = True

    # traverse for all DPi, j
    for i in range(len(s1)):
        for j in range(len(s2) + 1):

            # if possible for to convert i
            # characters of s1 to j characters
            # of s2
            if (dp[i][j]):

                # if upper_case(s1[i])==s2[j]
                # is same
                if ((j < len(s2) and
                     (s1[i].upper() == s2[j]))):
                    dp[i + 1][j + 1] = True

                # if not upper then deletion is
                # possible
                if (s1[i].isupper() == False):
                    dp[i + 1][j] = True
    return (dp[n][m])


# driver code
if __name__ == '__main__':

    s1 = "daBcd"
    s2 = "ABC"
    if (check(s1, s2)):
        print("YES")
    else:
        print("NO")
