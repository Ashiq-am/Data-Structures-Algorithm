# Python implementation
# to find the minimum
# and maximum amount

# import ceil function
from math import ceil


# function to find the maximum
# and the minimum cost required
def find(arr, n, k):
    # Sort the array
    arr.sort()
    b = int(ceil(n / k))

    # print the minimum cost
    print("minimum ", sum(arr[:b]))

    # print the maximum cost
    print("maximum ", sum(arr[-b:]))


# Driver Code
arr = [3, 2, 1, 4]
n = len(arr)
k = 2

# Function call
find(arr, n, k)
