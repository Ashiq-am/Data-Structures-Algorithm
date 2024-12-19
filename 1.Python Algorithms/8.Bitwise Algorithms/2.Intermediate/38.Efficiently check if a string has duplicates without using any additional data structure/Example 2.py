def unique(s):
    s = list(s)
    s.sort()
    for i in range(len(s) - 1):

        if (s[i] == s[i + 1]):
            return False
            break

    return True


if (unique("abcdd") == True):
    print("String is Unique")

else:
    print("String is not Unique")

# This code is contributed by shivanisinghss2110
