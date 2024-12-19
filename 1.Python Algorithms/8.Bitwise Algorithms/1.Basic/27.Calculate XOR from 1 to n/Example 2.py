# Python 3 Program to find
# XOR of numbers from 1 to n.

# Function to calculate xor
def computeXOR(n):
    # Modulus operator are expensive
    # on most of the computers. n & 3
    # will be equivalent to n % 4.

    # if n is multiple of 4
    if n % 4 == 0:
        return n

    # If n % 4 gives remainder 1
    if n % 4 == 1:
        return 1

    # If n%4 gives remainder 2
    if n % 4 == 2:
        return n + 1

    # If n%4 gives remainder 3
    return 0


# Driver Code
if __name__ == "__main__":
    n = 5

    # function calling
    print(computeXOR(n))

# This code is contributed by ANKITRAI1
