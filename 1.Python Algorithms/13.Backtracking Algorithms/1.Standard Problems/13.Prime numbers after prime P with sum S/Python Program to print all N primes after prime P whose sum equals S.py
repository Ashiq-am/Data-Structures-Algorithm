# Python Program to print
# all N primes after prime
# P whose sum equals S
import math

# vector to store prime
# and N primes whose
# sum equals given S
set = []
prime = []


# function to
# check prime number
def isPrime(x):
    # square root of x
    sqroot = int(math.sqrt(x))
    flag = True

    # since 1 is not
    # prime number
    if (x == 1):
        return False

    # if any factor is
    # found return false
    for i in range(2, sqroot + 1):
        if (x % i == 0):
            return False

    # no factor found
    return True


# function to display N
# primes whose sum equals S
def display():
    global set, prime
    length = len(set)
    for i in range(0, length):
        print(set[i], end=" ")
    print()


# function to evaluate
# all possible N primes
# whose sum equals S
def primeSum(total, N,
             S, index):
    global set, prime

    # if total equals S
    # And total is reached
    # using N primes
    if (total == S and
            len(set) == N):
        # display the N primes
        display()
        return

    # if total is greater
    # than S or if index
    # has reached last element
    if (total > S or
            index == len(prime)):
        return

    # add prime[index]
    # to set vector
    set.append(prime[index])

    # include the (index)th
    # prime to total
    primeSum(total + prime[index],
             N, S, index + 1)

    # remove element
    # from set vector
    set.pop()

    # exclude (index)th prime
    primeSum(total, N,
             S, index + 1)


# function to generate
# all primes
def allPrime(N, S, P):
    global set, prime

    # all primes less
    # than S itself
    for i in range(P + 1,
                   S + 1):

        # if i is prime add
        # it to prime vector
        if (isPrime(i)):
            prime.append(i)

        # if primes are
    # less than N
    if (len(prime) < N):
        return
    primeSum(0, N, S, 0)


# Driver Code
S = 54
N = 2
P = 3
allPrime(N, S, P)

# This code is contributed by
# Manish Shaw(manishshaw1)
