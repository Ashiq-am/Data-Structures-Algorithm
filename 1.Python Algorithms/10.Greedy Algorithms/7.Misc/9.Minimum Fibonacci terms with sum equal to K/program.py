# Python3 code to find minimum number
# of Fibonacci terms that sum to K.

# Function to calculate Fibonacci Terms
def calcFiboTerms(fiboTerms, K):
    i = 3
    fiboTerms.append(0)
    fiboTerms.append(1)
    fiboTerms.append(1)

    # Calculate all Fibonacci terms
    # which are less than or equal to K.
    while True:
        nextTerm = (fiboTerms[i - 1] +
                    fiboTerms[i - 2])

        # If next term is greater than K
        # do not push it in vector and return.
        if nextTerm > K:
            return

        fiboTerms.append(nextTerm)
        i += 1


# Function to find the minimum number of
# Fibonacci terms having sum equal to K.
def findMinTerms(K):
    # Vector to store Fibonacci terms.
    fiboTerms = []
    calcFiboTerms(fiboTerms, K)

    count, j = 0, len(fiboTerms) - 1

    # Subtract Fibonacci terms from
    # sum K until sum > 0.
    while K > 0:
        # Divide sum K by j-th Fibonacci
        # term to find how many terms it
        # contribute in sum.
        count += K // fiboTerms[j]
        K %= fiboTerms[j]

        j -= 1

    return count


# Driver code
if __name__ == "__main__":
    K = 17
    print(findMinTerms(K))
