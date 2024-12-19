# Python3 program to build levelwise
# OR/XOR alternating Segment tree
import math


# A utility function to get the
# middle index from corner indexes.
def getMid(s, e):
    return s + (e - s) // 2


# A recursive function that constructs
# Segment Tree for array[ss..se].
# 'si' is index of current node in segment
# tree 'st', operation denotes which operation
# is carried out at that level to merge the
# left and right child. It's either 0 or 1.
def constructSTUtil(arr, ss, se, st, si, operation):
    # If there is one element in array,
    # store it in current node of segment
    # tree and return
    if (ss == se):
        st[si] = arr[ss]
        return

    # If there are more than one elements,
    # then recur for left and right subtrees
    # and store the sum of values in this node
    mid = getMid(ss, se)

    # Build the left and the right subtrees by
    # using the fact that operation at level
    # (i + 1) = ! (operation at level i)
    constructSTUtil(arr, ss, mid, st,
                    si * 2 + 1, not operation)
    constructSTUtil(arr, mid + 1, se, st,
                    si * 2 + 2, not operation)

    # merge the left and right subtrees
    # by checking the operation to be
    # carried. If operation = 1, then
    # do OR else XOR
    if (operation == 1):

        # OR operation
        st[si] = (st[2 * si + 1] |
                  st[2 * si + 2])

    else:

        # XOR operation
        st[si] = (st[2 * si + 1] ^
                  st[2 * si + 2])


''' Function to construct segment tree
from given array. This function allocates
memory for segment tree and calls
constructSTUtil() to fill the allocated memory '''


def constructST(arr, n):
    # Allocate memory for segment tree

    # Height of segment tree
    x = int(math.ceil(math.log2(n)))

    # Maximum size of segment tree
    max_size = 2 * int(pow(2, x)) - 1

    # Allocate memory
    st = [0] * max_size

    # operation = 1(XOR) if Height of tree is
    # even else it is 0(OR) for the root node
    operationAtRoot = (0 if x % 2 == 0 else 1)

    # Fill the allocated memory st
    constructSTUtil(arr, 0, n - 1,
                    st, 0, operationAtRoot)

    # Return the constructed segment tree
    return st


# Driver Code
if __name__ == "__main__":
    # leaf nodes
    leaves = [1, 6, 3, 7, 5, 9, 10, 4]

    n = len(leaves)

    # Build the segment tree
    segmentTree = constructST(leaves, n)

    # Root node is at index 0 considering
    # 0-based indexing in segment Tree
    rootIndex = 0

    # print value at rootIndex
    print("Value at Root Node = ", segmentTree[rootIndex])
