# A backtracking based Python3 Program
# to fill two instances of all numbers
# from 1 to n in a specific way
def fillUtil(res, curr, n):
    # A recursive utility function to fill
    # two instances of numbers from 1 to n
    # in res[0..2n-1]. 'curr' is current value of n.

    # If current number becomes 0,
    # then all numbers are filled
    if curr == 0:
        return True

    # Try placing two instances of 'curr' at all
    # possible locations till solution is found
    for i in range(2 * n - curr - 1):

        # Two 'curr' should be placed
        # at 'curr+1' distance
        if res[i] == 0 and res[i + curr + 1] == 0:

            # Place two instances of 'curr'
            res[i] = res[i + curr + 1] = curr

            # Recur to check if the above
            # placement leads to a solution
            if fillUtil(res, curr - 1, n):
                return True

            # If solution is not possible,
            # then backtrack
            res[i] = 0
            res[i + curr + 1] = 0

    return False


def fill(n):
    # This function prints the result
    # for input number 'n' using fillUtil()

    # Create an array of size 2n and
    # initialize all elements in it as 0
    res = [0] * (2 * n)

    # If solution is possible, then print it.
    if fillUtil(res, n, n):
        for i in range(2 * n):
            print(res[i], end=' ')
        print()
    else:
        print("Not Possible")

    # Driver Code


if __name__ == '__main__':
    fill(7)

# This code is contributed by vibhu4agarwal
