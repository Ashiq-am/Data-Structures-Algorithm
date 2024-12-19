# Python program to compute sum of digits
# in numbers from 1 to n
import math


# Function to computer sum of digits in
# numbers from 1 to n
def sumOfDigitsFrom1ToN(n):
    d = int(math.log(n, 10))
    a = [0] * (d + 1)
    a[0] = 0
    a[1] = 45
    for i in range(2, d + 1):
        a[i] = a[i - 1] * 10 + 45 * \
               int(math.ceil(pow(10, i - 1)))

    return sumOfDigitsFrom1ToNUtil(n, a)


def sumOfDigitsFrom1ToNUtil(n, a):
    if (n < 10):
        return (n * (n + 1)) // 2

    d = int(math.log(n, 10))
    p = int(math.ceil(pow(10, d)))
    msd = n // p
    return (msd * a[d] + (msd * (msd - 1) // 2) * p +
            msd * (1 + n % p) + sumOfDigitsFrom1ToNUtil(n % p, a))


# Driver code
n = 328
print("Sum of digits in numbers from 1 to", n, "is", sumOfDigitsFrom1ToN(n))
