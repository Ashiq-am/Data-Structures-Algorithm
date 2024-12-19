# Python 3 code for Minimum Cost
# Required to connect weighted nodes
import sys


def minimum_cost(a, n):
    mn = sys.maxsize
    sum = 0
    for i in range(n):
        # To find the minimum element
        mn = min(a[i], mn)

        # sum of all the elements
        sum += a[i]

    return mn * (sum - mn)


# Driver code
if __name__ == "__main__":
    a = [4, 3, 2, 5]
    n = len(a)
    print(minimum_cost(a, n))

