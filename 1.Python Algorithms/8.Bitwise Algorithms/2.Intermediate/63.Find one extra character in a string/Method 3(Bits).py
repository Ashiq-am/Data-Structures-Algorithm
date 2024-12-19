# Python 3 program to find
# extra character in one string

def findExtraCharcter(strA, strB):
    # result store the result
    res = 0

    # traverse string A till
    # end and xor with res
    for i in range(0, len(strA)):
        # xor with res
        res = res ^ (ord)(strA[i])

    # traverse string B till
    # end and xor with res
    for i in range(0, len(strB)):
        # xor with res
        res = res ^ (ord)(strB[i])

    # print result at the end
    return ((chr)(res));


# given string
strA = "abcd"
strB = "cbdad"
print(findExtraCharcter(strA, strB))

# This code is contributed by Nikita Tiwari.
