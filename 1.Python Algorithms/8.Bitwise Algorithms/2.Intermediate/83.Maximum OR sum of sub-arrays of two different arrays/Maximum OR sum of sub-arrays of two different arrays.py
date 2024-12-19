# Python 3 program to
# find maximum OR sum

# function to find
# maximum OR sum
def MaximumSum(a, b, n):
    sum1 = 0
    sum2 = 0

    # OR sum of all the
    # elements in both arrays
    for i in range(0, n):
        sum1 |= a[i]
        sum2 |= b[i]

    print(sum1 + sum2)


# Driver Code
A = [1, 2, 4, 3, 2]
B = [2, 3, 3, 12, 1]
n = len(A)

MaximumSum(A, B, n)

# This code is contributed by Smitha Dinesh Semwal
