# Python 3 program to count the number of
# unique triplets whose XOR is 0

# function to count the number of
# unique triplets whose xor is 0
def countTriplets(a, n):
    # To store values that are present
    s = set()
    for i in range(n):
        s.add(a[i])

    # stores the count of unique triplets
    count = 0

    # traverse for all i, j pairs such that j>i
    for i in range(n):
        for j in range(i + 1, n, 1):

            # xor of a[i] and a[j]
            xr = a[i] ^ a[j]

            # if xr of two numbers is present,
            # then increase the count
            if (xr in s and xr != a[i] and
                    xr != a[j]):
                count += 1;

    # returns answer
    return int(count / 3)


# Driver code
if __name__ == '__main__':
    a = [1, 3, 5, 10, 14, 15]
    n = len(a)
    print(countTriplets(a, n))

# This code is contributed by
# Surendra_Gangwar
