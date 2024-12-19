# Python program to find n-th palindrome

# utility function which is used to
# convert binary string into integer
def convertStringToInt(s):
    ans = 0

    # convert binary string into integer
    for i in range(len(s)):
        ans = ans * 2 + (ord(s[i]) - ord('0'))

    return ans


# function to find nth binary palindrome number
def getNthNumber(n):
    # stores the binary palindrome string
    q = []

    # base case
    if (n == 1):
        return 1
    n = n - 1

    # add 2nd binary palindrome string
    q.append("11")

    # runs till the nth binary palindrome number
    while (len(q) != 0):

        # remove curr binary palindrome string from
        # queue
        curr = q.pop(0)
        n -= 1

        # if n==0 then we find the n'th binary
        # palindrome so we return our answer
        if (n == 0):
            return convertStringToInt(curr)

        # calculate length of curr binary palindrome
        # string
        lenn = len(curr)

        # if length is even .so it is our first case
        # we have two choices
        if (len(curr) % 2 == 0):
            q.append(curr[0:int(lenn / 2)] + "0" + curr[int(lenn / 2):])
            q.append(curr[0:int(lenn / 2)] + "1" + curr[int(lenn / 2):])

        # if length is odd .so it is our second case
        # we have only one choice
        else:
            midChar = curr[int(lenn / 2)]
            q.append(curr[0:int(lenn / 2)] + midChar + curr[int(lenn / 2):])

    return 0


# Driver code
n = 9

# Function Call
print(getNthNumber(n))
