# Python3 program to print the Leftover element
# after performing alternate Bitwise OR and
# Bitwise XOR operations to the pairs.
N = 1000


def lastElement(a, n):
    # count the step number
    steps = 1
    v = [[] for i in range(n)]

    # if one element is there, it will be the answer
    if n == 1: return a[0]

    # at first step we do a bitwise OR
    for i in range(0, n, 2):
        v[steps].append(a[i] | a[i + 1])

    # keep on doing bitwise operations
    # till the last element is left
    while len(v[steps]) > 1:

        steps += 1
        # perform operations
        for i in range(0, len(v[steps - 1]), 2):

            # if step is the odd step
            if steps & 1:
                v[steps].append(v[steps - 1][i] | v[steps - 1][i + 1])
            else:  # even step
                v[steps].append(v[steps - 1][i] ^ v[steps - 1][i + 1])

    # answer when one element is left
    return v[steps][0]


# Driver Code
if __name__ == "__main__":
    a = [1, 4, 5, 6]
    n = len(a)

    # 1st query
    index, value, a[0] = 0, 2, 2
    print(lastElement(a, n))

    # 2nd query
    index, value = 3, 5
    value = 5
    a[index] = value
    print(lastElement(a, n))
