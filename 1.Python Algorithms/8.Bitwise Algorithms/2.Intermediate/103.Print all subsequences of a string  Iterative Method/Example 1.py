# Python3 program to print all Subsequences
# of a string in iterative manner

# function to find subsequence
def subsequence(s, binary, length):
    sub = ""
    for j in range(length):

        # check if jth bit in binary is 1
        if (binary & (1 << j)):
            # if jth bit is 1, include it
            # in subsequence
            sub += s[j]
    return sub


# function to print all subsequences
def possibleSubsequences(s):
    # map to store subsequence
    # lexicographically by length
    sorted_subsequence = {}

    length = len(s)

    # Total number of non-empty subsequence
    # in string is 2^len-1
    limit = 2 ** length

    # i=0, corresponds to empty subsequence
    for i in range(1, limit):

        # subsequence for binary pattern i
        sub = subsequence(s, i, length)

        # storing sub in map
        if len(sub) in sorted_subsequence.keys():
            sorted_subsequence[len(sub)] = \
                tuple(list(sorted_subsequence[len(sub)]) + [sub])
        else:
            sorted_subsequence[len(sub)] = [sub]

    for it in sorted_subsequence:

        # it.first is length of Subsequence
        # it.second is set<string>
        print("Subsequences of length =", it, "are:")
        for ii in sorted(set(sorted_subsequence[it])):
            # ii is iterator of type set<string>
            print(ii, end=' ')
        print()


# Driver Code
s = "aabc"
possibleSubsequences(s)

# This code is contributed by ankush_953
