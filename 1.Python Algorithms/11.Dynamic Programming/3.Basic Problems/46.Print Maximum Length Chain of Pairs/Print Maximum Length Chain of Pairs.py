# Dynamic Programming solution to construct
# Maximum Length Chain of Pairs
class Pair:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __lt__(self, other):
        return self.a < other.a


def maxChainLength(arr):
    # Function to construct
    # Maximum Length Chain of Pairs

    # Sort by start time
    arr.sort()

    # L[i] stores maximum length of chain of
    # arr[0..i] that ends with arr[i].
    L = [[] for x in range(len(arr))]

    # L[0] is equal to arr[0]
    L[0].append(arr[0])

    # start from index 1
    for i in range(1, len(arr)):

        # for every j less than i
        for j in range(i):

            # L[i] = {Max(L[j])} + arr[i]
            # where j < i and arr[j].b < arr[i].a
            if (arr[j].b < arr[i].a and
                    len(L[j]) > len(L[i])):
                L[i] = L[j]

        L[i].append(arr[i])

    # print max length vector
    maxChain = []
    for x in L:
        if len(x) > len(maxChain):
            maxChain = x

    for pair in maxChain:
        print("({a},{b})".format(a=pair.a,
                                 b=pair.b),
              end=" ")
    print()


# Driver Code
if __name__ == "__main__":
    arr = [Pair(5, 29), Pair(39, 40),
           Pair(15, 28), Pair(27, 40),
           Pair(50, 90)]
    n = len(arr)
    maxChainLength(arr)
