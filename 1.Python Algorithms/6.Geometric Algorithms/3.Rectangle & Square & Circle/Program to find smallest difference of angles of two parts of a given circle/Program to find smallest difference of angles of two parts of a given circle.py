# Python program to find minimum
# difference of angles of two
# parts of given circle.
import math


# function returns the minimum
# difference of angles.
def findMinimumAngle(arr, n):
    l = 0
    _sum = 0
    ans = 360
    for i in range(n):

        # sum of array
        _sum += arr[i]

        while _sum >= 180:
            # calculating the difference of
            # angles and take minimum of
            # previous and newly calculated
            ans = min(ans, 2 * abs(180 - _sum))
            _sum -= arr[l]
            l += 1
        ans = min(ans, 2 * abs(180 - _sum))
    return ans


# driver code
arr = [100, 100, 160]
n = len(arr)
print(findMinimumAngle(arr, n))

# This code is contributed by "Abhishek Sharma 44"
