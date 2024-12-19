# Python3 program to find minimum time
# required to produce m items.
import math as mt


# Return the minimum time required to
# produce m items with given machines.
def minTime(arr, n, m):
    # Intialise time, items equal to 0.
    t = 0

    while (1):

        items = 0

        # Calculating items at each second
        for i in range(n):
            items += (t // arr[i])

        # If items equal to m return time.
        if (items >= m):
            return t

        t += 1  # Increment time


# Driver Code
arr = [1, 2, 3]
n = len(arr)
m = 11

print(minTime(arr, n, m))
