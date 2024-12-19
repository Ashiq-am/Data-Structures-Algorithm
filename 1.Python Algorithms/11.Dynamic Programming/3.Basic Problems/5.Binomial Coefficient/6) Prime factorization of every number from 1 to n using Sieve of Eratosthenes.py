# Python code for the above approach
import math


class GFG:
    def nCr(self, n, r):

        # Base case
        if r > n:
            return 0

        # C(n,r) = C(n,n-r) Complexity for this
        # code is lesser for lower n-r
        if n - r > r:
            r = n - r

        # List to store smallest prime factor
        # of every number from 1 to n
        SPF = [i for i in range(n + 1)]
        for i in range(4, n + 1, 2):
            # set smallest prime factor of
            # all even numbers as 2
            SPF[i] = 2

        for i in range(3, n + 1, 2):

            if i * i > n:
                break

            # Check if i is prime
            if SPF[i] == i:

                # All multiples of i are composite
                # (and divisible by i) so add i to
                # their prime factorization getpow(j,i) times
                for j in range(i * i, n + 1, i):
                    if SPF[j] == j:
                        # set smallest prime factor
                        # of j to i only if it is
                        # not previously set
                        SPF[j] = i

        # dictionary to store power of each prime in C(n,r)
        prime_pow = {}

        # For numerator count frequency
        # of each prime factor
        for i in range(r + 1, n + 1):
            t = i

            # Recursive division to
            # find prime factorization of i
            while t > 1:
                if not SPF[t] in prime_pow:
                    prime_pow[SPF[t]] = 1
                else:
                    prime_pow[SPF[t]] += 1
                t //= SPF[t]

        # For denominator subtract the
        # power of each prime factor
        for i in range(1, n - r + 1):
            t = i

            # Recursive division to
            # find prime factorization of i
            while t > 1:
                prime_pow[SPF[t]] -= 1
                t //= SPF[t]
        ans = 1
        mod = 10 ** 9 + 7

        # Use (a*b)%mod = (a%mod * b%mod)%mod
        for i in prime_pow:
            # pow(base,exp,mod) is used to
            # find (base^exp)%mod fast
            ans = (ans * pow(i, prime_pow[i], mod)) % mod
        return ans


# Driver code
n = 5
k = 2
ob = GFG()
print("Value of C(" + str(n) +
      ", " + str(k) + ") is",
      ob.nCr(n, k))
