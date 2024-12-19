# An LCS based Python3 program to find minimum
# number insertions needed to make a string
# palindrome

""" Returns length of LCS for X[0..m-1],
Y[0..n-1]. See http://goo.gl/bHQVP for
details of this function """


def lcs(X, Y, m, n):
    L = [[0 for i in range(n + 1)] for j in range(m + 1)]

    """ Following steps build L[m + 1, n + 1] in
    bottom up fashion. Note that L[i, j]
    contains length of LCS of X[0..i - 1]
    and Y[0..j - 1] """
    for i in range(m + 1):
        for j in range(n + 1):
            if (i == 0 or j == 0):
                L[i][j] = 0

            elif (X[i - 1] == Y[j - 1]):
                L[i][j] = L[i - 1][j - 1] + 1
            else:
                L[i][j] = max(L[i - 1][j], L[i][j - 1])

    """ L[m,n] contains length of LCS for
    X[0..n-1] and Y[0..m-1] """
    return L[m][n]


# LCS based function to find minimum number
# of insertions
def findMinInsertionsLCS(Str, n):
    # Using charArray to reverse a String
    charArray = list(Str)
    charArray.reverse()
    revString = "".join(charArray)

    # The output is length of string minus
    # length of lcs of str and it reverse
    return (n - lcs(Str, revString, n, n))


# Driver code
Str = "geeks"
print(findMinInsertionsLCS(Str, len(Str)))
