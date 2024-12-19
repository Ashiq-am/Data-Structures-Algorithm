# A Naive recursive Python3
# code to find if given string
# is K-Palindrome or not

# Find if given string
# is K-Palindrome or not
def isKPalRec(str1, str2, m, n):
    # If first string is empty,
    # the only option is to remove
    # all characters of second string
    if not m: return n

    # If second string is empty,
    # the only option is to remove
    # all characters of first string
    if not n: return m

    # If last characters of two strings
    # are same, ignore last characters
    # and get count for remaining strings.
    if str1[m - 1] == str2[n - 1]:
        return isKPalRec(str1, str2, m - 1, n - 1)

    # If last characters are not same,
    # 1. Remove last char from str1 and recur for m-1 and n
    # 2. Remove last char from str2 and recur for m and n-1
    # Take minimum of above two operations
    res = 1 + min(isKPalRec(str1, str2, m - 1, n),  # Remove from str1
                  (isKPalRec(str1, str2, m, n - 1)))  # Remove from str2

    return res


# Returns true if str is k palindrome.
def isKPal(string, k):
    revStr = string[::-1]
    l = len(string)

    return (isKPalRec(string, revStr, l, l) <= k * 2)


# Driver program
string = "acdcb"
k = 2

print("Yes" if isKPal(string, k) else "No")
