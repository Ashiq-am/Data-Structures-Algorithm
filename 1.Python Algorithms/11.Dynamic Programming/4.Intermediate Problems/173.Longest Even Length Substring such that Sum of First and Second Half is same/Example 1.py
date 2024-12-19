# A simple Python 3 based
# program to find length
# of longest even length
# substring with same sum
# of digits in left and right

def findLength(str):
    n = len(str)
    maxlen = 0  # Initialize result

    # Choose starting point
    # of every substring
    for i in range(0, n):

        # Choose ending point
        # of even length substring
        for j in range(i + 1, n, 2):

            # Find length of current substr
            length = j - i + 1

            # Calculate left & right
            # sums for current substr
            leftsum = 0
            rightsum = 0
            for k in range(0, int(length / 2)):
                leftsum += (int(str[i + k]) - int('0'))
                rightsum += (int(str[i + k + int(length / 2)]) - int('0'))

            # Update result if needed
            if (leftsum == rightsum and maxlen < length):
                maxlen = length

    return maxlen


# Driver program to
# test above function
str = "1538023"
print("Length of the substring is",
      findLength(str))
