# Python3 program to print the largest palindromic
# number by permuting digits of a number
from collections import defaultdict


# Function to check if a number can be
# permuted to form a palindrome number
def possibility(m, length, s):
    # counts the occurrence of
    # number which is odd
    countodd = 0
    for i in range(0, length):

        # if occurrence is odd
        if m[int(s[i])] & 1:
            countodd += 1

        # if number exceeds 1
        if countodd > 1:
            return False

    return True


# Function to print the largest palindromic
# number by permuting digits of a number
def largestPalindrome(s):
    # string length
    l = len(s)

    # map that marks the occurrence of a number
    m = defaultdict(lambda: 0)
    for i in range(0, l):
        m[int(s[i])] += 1

    # check the possibility of a
    # palindromic number
    if possibility(m, l, s) == False:
        print("Palindrome cannot be formed")
        return

    # string array that stores the largest
    # permuted palindromic number
    largest = [None] * l

    # pointer of front
    front = 0

    # greedily start from 9 to 0 and place the
    # greater number in front and odd in the middle
    for i in range(9, -1, -1):

        # if the occurrence of number is odd
        if m[i] & 1:

            # place one odd occurring number
            # in the middle
            largest[l // 2] = chr(i + 48)

            # decrease the count
            m[i] -= 1

            # place the rest of numbers greedily
            while m[i] > 0:
                largest[front] = chr(i + 48)
                largest[l - front - 1] = chr(i + 48)
                m[i] -= 2
                front += 1

        else:

            # if all numbers occur even times,
            # then place greedily
            while m[i] > 0:
                # place greedily at front
                largest[front] = chr(i + 48)
                largest[l - front - 1] = chr(i + 48)

                # 2 numbers are placed,
                # so decrease the count
                m[i] -= 2

                # increase placing position
                front += 1

    # print the largest string thus formed
    for i in range(0, l):
        print(largest[i], end="")


# Driver Code
if __name__ == "__main__":
    s = "313551"
    largestPalindrome(s)
