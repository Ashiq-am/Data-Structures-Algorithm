# Python3 program to count the
# number of composite numbers
# in the given array

# Function that returns the
# the count of composite numbers
def compositeCount(arr, n):
    Sum = 0

    # Find maximum value in the array
    max_val = max(arr)

    # Use sieve to find all prime numbers
    # less than or equal to max_val
    # Create a boolean array "prime[0..n]".
    # A value in prime[i] will finally be
    # false if i is Not a prime, else True.
    prime = [True for i in range(max_val + 1)]

    # Set 0 and 1 as primes as
    # they don't need to be
    # counted as composite numbers
    prime[0] = True
    prime[1] = True
    for p in range(2, max_val + 1):

        if p * p > max_val:
            break

        # If prime[p] is not changed,
        # then it is a prime
        if (prime[p] == True):

            # Update all multiples of p
            for i in range(p * 2, max_val + 1, p):
                prime[i] = False

    # Count all composite numbers
    # in the arr[]
    count = 0
    for i in range(n):
        if (prime[arr[i]] == False):
            count += 1
            Sum = Sum + arr[i]

    return count, Sum


# Driver code
arr = [1, 2, 3, 4, 5, 6, 7]
n = len(arr)
count, Sum = compositeCount(arr, n)

print("Count of Composite Numbers = ", count)

print("Sum of Composite Numbers = ", Sum)


