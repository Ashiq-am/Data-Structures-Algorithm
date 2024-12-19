# Python3 program to find maximum
# integer possible by doing at-most
# K swap operations on its digits.

# utility function to swap two
# characters of a string
def swap(string, i, j):
    return (string[:i] + string[j] +
            string[i + 1:j] +
            string[i] + string[j + 1:])


# function to find maximum integer
# possible by doing at-most K swap
# operations on its digits
def findMaximumNum(string, k, maxm):
    # return if no swaps left
    if k == 0:
        return

    n = len(string)

    # consider every digit
    for i in range(n - 1):

        # and compare it with all digits after it
        for j in range(i + 1, n):

            # if digit at position i is less than
            # digit at position j, swap it and
            # check for maximum number so far and
            # recurse for remaining swaps
            if string[i] < string[j]:

                # swap string[i] with string[j]
                string = swap(string, i, j)

                # If current num is more than
                # maximum so far
                if string > maxm[0]:
                    maxm[0] = string

                # recurse of the other k - 1 swaps
                findMaximumNum(string, k - 1, maxm)

                # backtrack
                string = swap(string, i, j)

            # Driver Code


if __name__ == "__main__":
    string = "129814999"
    k = 4
    maxm = [string]
    findMaximumNum(string, k, maxm)
    print(maxm[0])

# This code is contributed
# by vibhu4agarwal
