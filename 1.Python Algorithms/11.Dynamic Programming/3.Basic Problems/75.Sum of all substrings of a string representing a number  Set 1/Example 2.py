# Python3 program to print sum of all substring of
# a number represented as a string

# Returns sum of all substring of num
def sumOfSubstrings(num):
    n = len(num)

    # storing prev value
    prev = int(num[0])

    res = prev  # ans

    current = 0

    # substrings sum upto current index
    # loop over all digits of string
    for i in range(1, n):
        numi = int(num[i])

        # update each sumofdigit from previous value
        current = (i + 1) * numi + 10 * prev

        # add current value to the result
        res += current
        prev = current  # update previous

    return res


num = "1234"
print(sumOfSubstrings(num))
