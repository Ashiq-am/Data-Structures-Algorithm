# Python3 program to illustrate string
# with unique characters using
# brute force technique
def uniqueCharacters(st):
    # Using sorting
    st = sorted(st)

    for i in range(len(st) - 1):

        # if at any time, 2 adjacent
        # elements become equal,
        # return false
        if (st[i] == st[i + 1]):
            return False

    return True


# Driver code
if __name__ == '__main__':

    st = "GeeksforGeeks"

    if (uniqueCharacters(st)):
        print("The String", st, "has all unique characters\n")

    else:
        print("The String", st, "has duplicate characters\n")

# This code is contributed by AbhiThakur
