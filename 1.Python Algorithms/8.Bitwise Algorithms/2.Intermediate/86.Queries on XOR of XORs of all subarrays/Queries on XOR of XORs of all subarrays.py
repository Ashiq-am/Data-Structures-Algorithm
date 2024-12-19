# Python 3 Program to answer queries on
# XOR of XORs of all subarray
N = 100


# Output for each query
def ansQueries(prefeven, prefodd, l, r):
    # If number of element is even.
    if ((r - l + 1) % 2 == 0):
        print("0")

    # If number of element is odd.
    else:

        # if l is even
        if (l % 2 == 0):
            print(prefeven[r] ^
                  prefeven[l - 1])

        # if l is odd
        else:
            print(prefodd[r] ^
                  prefodd[l - 1])


# Wrapper Function
def wrapper(arr, n, l, r, q):
    prefodd = [0] * N
    prefeven = [0] * N

    # Evaluating prefixodd and prefixeven
    for i in range(1, n + 1):
        if ((i) % 2 == 0):
            prefeven[i] = arr[i - 1] ^ prefeven[i - 1]
            prefodd[i] = prefodd[i - 1]

        else:
            prefeven[i] = prefeven[i - 1]
            prefodd[i] = prefodd[i - 1] ^ arr[i - 1]

    i = 0
    while (i != q):
        ansQueries(prefeven, prefodd, l[i], r[i])
        i += 1


# Driver Code
if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    n = len(arr)

    l = [1, 1, 2]
    r = [2, 3, 4]
    q = len(l)

    wrapper(arr, n, l, r, q)

# This code is contributed by ita_c
