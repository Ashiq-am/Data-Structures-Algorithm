'''
Python3 program to find product of
all the composite numberes in given array'''
import math as mt

'''
function to find the product of all composite
niumbers in the given array
'''


def compositeProduct(arr, n):
    # find the maximum value in the array
    max_val = max(arr)
    '''
    USE SIEVE TO FIND ALL PRIME NUMBERS LESS
    THAN OR EQUAL TO max_val
    Create a boolean array "prime[0..n]". A
    value in prime[i] will finally be false
    if i is Not a prime, else true.
    '''
    prime = [True for i in range(max_val + 1)]

    '''
    Set 0 and 1 as primes as
    they don't need to be
    counted as composite numbers
    '''
    prime[0] = True
    prime[1] = True

    for p in range(2, mt.ceil(mt.sqrt(max_val))):
        # Remaining part of SIEVE
        '''
        if prime[p] is not changed, than it is prime
        '''
        if prime[p]:
            # update all multiples of p
            for i in range(p * 2, max_val + 1, p):
                prime[i] = False

    # find the product of all composite numbers in the arr[]
    product = 1

    for i in range(n):
        if prime[arr[i]] == False:
            product *= arr[i]

    return product


# Driver code

arr = [2, 3, 4, 5, 6, 7]

n = len(arr)

print(compositeProduct(arr, n))

