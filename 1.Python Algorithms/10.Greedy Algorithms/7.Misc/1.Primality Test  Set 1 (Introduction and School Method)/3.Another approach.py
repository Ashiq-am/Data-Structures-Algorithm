# Python program to check the given number
# is prime or not

# Function to check if the given number
# is prime or not.
import math


def isPrime(n):
    if n == 2 or n == 3:
        return True
    elif n <= 1 or n % 2 == 0 or n % 3 == 0:
        return False

    # To check through all numbers of the form 6k ± 1
    # until i <= square root of n, with step value 6
    for i in range(5, int(math.sqrt(n)) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False

    return True


# # Driver code
print(isPrime(11))
print(isPrime(20))

# # This code is contributed by Harsh Master
