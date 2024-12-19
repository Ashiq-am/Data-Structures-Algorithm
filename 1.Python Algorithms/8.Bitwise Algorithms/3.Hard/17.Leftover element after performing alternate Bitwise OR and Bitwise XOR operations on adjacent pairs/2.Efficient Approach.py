# Python3 program to print the Leftover element
# after performing alternate Bitwise OR and
# Bitwise XOR operations to the pairs.
N = 1000

# array to store the tree
tree = [None] * N

# array to store the level of every parent
level = [None] * N


# function to construct the tree
def constructTree(low, high, pos, a):
    if low == high:
        # level of child is always 0
        level[pos], tree[pos] = 0, a[high]
        return

    mid = (low + high) // 2

    # Recursive call
    constructTree(low, mid, 2 * pos + 1, a)
    constructTree(mid + 1, high, 2 * pos + 2, a)

    # Increase the level of every parent,
    # which is level of child + 1
    level[pos] = level[2 * pos + 1] + 1

    # If the parent is at odd level,
    # then do a bitwise OR
    if level[pos] & 1:
        tree[pos] = tree[2 * pos + 1] | tree[2 * pos + 2]

    # If the parent is at even level,
    # then do a bitwise XOR
    else:
        tree[pos] = tree[2 * pos + 1] ^ tree[2 * pos + 2]


# Function that updates the tree
def update(low, high, pos, index, a):
    # If it is a leaf and the leaf
    # which is to be updated
    if low == high and low == index:
        tree[pos] = a[low]
        return

    # out of range
    if index < low or index > high:
        return

    # not a leaf then recurse
    if low != high:

        mid = (low + high) // 2

        # recursive call
        update(low, mid, 2 * pos + 1, index, a)
        update(mid + 1, high, 2 * pos + 2, index, a)

        # check if the parent is at odd or even level
        # and perform OR or XOR according to that
        if level[pos] & 1:
            tree[pos] = tree[2 * pos + 1] | tree[2 * pos + 2]
        else:
            tree[pos] = tree[2 * pos + 1] ^ tree[2 * pos + 2]


# Function that assigns value to a[index]
# and calls update function to update the tree
def updateValue(index, value, a, n):
    a[index] = value
    update(0, n - 1, 0, index, a)


# Driver Code
if __name__ == "__main__":
    a = [1, 4, 5, 6]
    n = len(a)

    # builds the tree
    constructTree(0, n - 1, 0, a)

    # 1st query
    index, value = 0, 2
    updateValue(index, value, a, n)
    print(tree[0])

    # 2nd query
    index, value = 3, 5
    updateValue(index, value, a, n)
    print(tree[0])
