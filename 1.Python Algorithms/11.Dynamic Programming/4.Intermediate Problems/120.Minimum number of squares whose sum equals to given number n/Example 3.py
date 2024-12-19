import sys


def minCount(n):
    minSquaresRequired = [0 for i in range(n + 1)]

    minSquaresRequired[0] = 0

    minSquaresRequired[1] = 1

    for i in range(2, n + 1):

        minSquaresRequired[i] = sys.maxsize
        j = 1

        for j in range(1, i - (j * j)):
            if (i - (j * j) >= 0):
                minSquaresRequired[i] = min(minSquaresRequired[i], minSquaresRequired[i - (j * j)]);
            else:
                break

        minSquaresRequired[i] += 1

    result = minSquaresRequired[n]

    return result


# Driver code
if __name__ == '__main__':
    print(minCount(6))


