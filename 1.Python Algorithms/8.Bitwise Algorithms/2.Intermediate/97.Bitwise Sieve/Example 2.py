# Python3 program to implement
# bitwise Sieve of Eratosthenes.

# Checks whether x is
# prime or composite
def ifnotPrime(prime, x):
    # Checking whether the value
    # of element is set or not.
    # Using prime[x/64], we find
    # the slot in prime array.
    # To find the bit we divide
    # x by 2 and take its mod
    # with 32.
    return (prime[int(x / 64)] &
            (1 << ((x >> 1) & 31)))


# Marks x composite in prime[]
def makeComposite(prime, x):
    # Set a bit corresponding to
    # given element. Using prime[x/64],
    # we find the slot in prime array.
    # To find the bit number, we divide x
    # by 2 and take its mod with 32.
    prime[int(x / 64)] |= (1 << ((x >> 1) & 31))


# Prints all prime numbers
# smaller than n.
def bitWiseSieve(n):
    # Assuming that n takes 32 bits,
    # we reduce size to n/64 from n/2.
    # Initializing values to 0.
    prime = [0 for i in range(int(n / 64) + 1)]

    # 2 is the only even prime so
    # we can ignore that loop
    # starts from 3 as we have used
    # in sieve of Eratosthenes
    for i in range(3, n + 1, 2):
        if (i * i <= n):

            # If i is prime, mark all
            # its multiples as composite
            if (ifnotPrime(prime, i)):
                continue
            else:
                k = i << 1
                for j in range(i * i, n, k):
                    k = i << 1
                    makeComposite(prime, j)

    # Writing 2 separately
    print("2 ", end="")

    # Printing other primes
    for i in range(3, n + 1, 2):
        if (ifnotPrime(prime, i)):
            continue
        else:
            print(i, end=" ")


# Driver code
n = 30
bitWiseSieve(n)

# This code is contributed by avanitrachhadiya2155
