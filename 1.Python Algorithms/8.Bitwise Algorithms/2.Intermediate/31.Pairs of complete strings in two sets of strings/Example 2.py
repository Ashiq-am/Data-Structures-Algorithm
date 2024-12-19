# Python3 program to find count of complete pairs

# Returns count of complete pairs from set[0..n-1]
# and set2[0..m-1]
def countCompletePairs(set1, set2, n, m):
    result = 0

    # con_s1[i] is going to store an integer whose
    # set bits represent presence/absence of characters
    # in set1[i].
    # Similarly con_s2[i] is going to store an integer
    # whose set bits represent presence/absence of
    # characters in set2[i]
    con_s1, con_s2 = [0] * n, [0] * m

    # Process all strings in set1[]
    for i in range(n):

        # initializing all bits to 0
        con_s1[i] = 0
        for j in range(len(set1[i])):
            # Setting the ascii code of char s[i][j]
            # to 1 in the compressed integer.
            con_s1[i] = con_s1[i] | (1 << (ord(set1[i][j]) - ord('a')))

    # Process all strings in set2[]
    for i in range(m):

        # initializing all bits to 0
        con_s2[i] = 0
        for j in range(len(set2[i])):
            # setting the ascii code of char s[i][j]
            # to 1 in the compressed integer.
            con_s2[i] = con_s2[i] | (1 << (ord(set2[i][j]) - ord('a')))

    # assigning a variable whose all 26 (0..25)
    # bits are set to 1
    complete = (1 << 26) - 1

    # Now consider every pair of integer in con_s1[]
    # and con_s2[] and check if the pair is complete.
    for i in range(n):
        for j in range(m):

            # if all bits are set, the strings are
            # complete!
            if ((con_s1[i] | con_s2[j]) == complete):
                result += 1

    return result


# Driver code
if __name__ == '__main__':
    set1 = ["abcdefgh", "geeksforgeeks",
            "lmnopqrst", "abc"]
    set2 = ["ijklmnopqrstuvwxyz",
            "abcdefghijklmnopqrstuvwxyz",
            "defghijklmnopqrstuvwxyz"]
    n = len(set1)
    m = len(set2)

    print(countCompletePairs(set1, set2, n, m))

# This code is contributed by mohit kumar 29
