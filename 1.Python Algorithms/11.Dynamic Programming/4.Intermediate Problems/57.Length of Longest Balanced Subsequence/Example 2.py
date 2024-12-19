# Python3 program to find length of
# the longest balanced subsequence

def maxLength(s, n):
    # As it's subsequence - assuming first
    # open brace would map to a first close
    # brace which occurs after the open brace
    # to make subsequence balanced and second
    # open brace would map to second close
    # brace and so on.

    # Variable to count all the open brace
    # that does not have the corresponding
    # closing brace.
    invalidOpenBraces = 0;

    # To count all the close brace that does
    # not have the corresponding open brace.
    invalidCloseBraces = 0;

    # Iterating over the String
    for i in range(n):
        if (s[i] == '('):

            # Number of open braces that
            # hasn't been closed yet.
            invalidOpenBraces += 1
        else:
            if (invalidOpenBraces == 0):
                # Number of close braces that
                # cannot be mapped to any open
                # brace.
                invalidCloseBraces += 1
            else:
                # Mapping the ith close brace
                # to one of the open brace.
                invalidOpenBraces -= 1

    return (
            n - (
            invalidOpenBraces + invalidCloseBraces))


# Driver Code
s = "()(((((()"
n = len(s)
print(maxLength(s, n))
