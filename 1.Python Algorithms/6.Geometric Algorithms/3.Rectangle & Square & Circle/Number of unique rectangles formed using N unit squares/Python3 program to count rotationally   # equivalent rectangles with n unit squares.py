# Python3 program to count rotationally
# equivalent rectangles with n unit squares
import math


def countRect(n):
    ans = 0
    for length in range(1, int(math.sqrt(n)) + 1):
        height = length
        while (height * length <= n):
            # height >= length is maintained
            ans += 1
            height += 1
    return ans


# Driver code
n = 5
print(countRect(n))

# This code is contributed by Anant Agarwal.
