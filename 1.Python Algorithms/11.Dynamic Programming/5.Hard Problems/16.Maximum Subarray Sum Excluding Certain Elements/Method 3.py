# Python3 program implementation of the
# above idea
import sys


# Function to calculate the max sum of
# contiguous subarray of B whose elements
# are not present in A
def findMaxSubarraySum(A, B):
    m = dict()

    # Mark all the elements present in B
    for i in range(len(B)):
        if B[i] not in m:
            m[B[i]] = 0

        m[B[i]] = 1

    # Initialize max_so_far with INT_MIN
    max_so_far = -sys.maxsize - 1
    currmax = 0

    # Traverse the array A
    for i in range(len(A)):
        if (currmax < 0 or (A[i] in m and m[A[i]] == 1)):
            currmax = 0
            continue

        currmax = max(A[i], A[i] + currmax)

        # If current max is greater than
        # max so far then update max so far
        if (max_so_far < currmax):
            max_so_far = currmax

    return max_so_far


# Driver Code
if __name__ == '__main__':
    a = [3, 4, 5, -4, 6]
    b = [1, 8, 5]

    # Function call
    print(findMaxSubarraySum(a, b))
