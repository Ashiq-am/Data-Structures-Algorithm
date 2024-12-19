# Python3 program to find smallest possible
# length of a string of only three characters

# Returns smallest possible length
# with given operation allowed.
def stringReduction(str):
    n = len(str)

    # Counint occurrences of three different
    # characters 'a', 'b' and 'c' in str
    count = [0] * 3
    for i in range(n):
        count[ord(str[i]) - ord('a')] += 1

    # If all characters are same.
    if (count[0] == n or count[1] == n or
            count[2] == n):
        return n

    # If all characters are present even number
    # of times or all are present odd number of
    # times.
    if ((count[0] % 2) == (count[1] % 2) and
            (count[1] % 2) == (count[2] % 2)):
        return 2

    # Answer is 1 for all other cases.
    return 1


# Driver code
if __name__ == "__main__":
    str = "abcbbaacb"
    print(stringReduction(str))

# This code is contributed by ita_c
