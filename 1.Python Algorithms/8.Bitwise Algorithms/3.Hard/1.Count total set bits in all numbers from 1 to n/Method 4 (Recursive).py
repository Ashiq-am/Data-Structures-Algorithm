def findLargestPower(n):
    x = 0
    while ((1 << x) <= n):
        x += 1
    return x - 1


def countSetBits(n):
    if (n <= 1):
        return n
    x = findLargestPower(n)
    return (x * pow(2, (x - 1))) + (n - pow(2, x) + 1) + countSetBits(n - pow(2, x))


N = 17
print(countSetBits(N))

# This code is contributed by shivanisinghss2110
