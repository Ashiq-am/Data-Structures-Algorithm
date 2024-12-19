# Python3 program to return minimum number of elements which
# are not part of increasing or decreasing subsequences.
MAX = 102


# Return minimum number of elements which is not part of
# any of the sequence.

def countMin(arr, dp, n, dec, inc, i):
    # If already calculated, return value.
    if dp[dec][inc][i] != -1:
        return dp[dec][inc][i]

    # If whole array is traversed.
    if i == n:
        return 0

    # calculating by considering element as part of
    # decreasing sequence.
    if arr[i] < arr[dec]:
        dp[dec][inc][i] = countMin(arr, dp, n, i, inc, i + 1)

    # calculating by considering
    # element as part of
    # increasing sequence.
    if arr[i] > arr[inc]:

        # If cannot be calculated for
        # decreasing sequence.
        if dp[dec][inc][i] == -1:
            dp[dec][inc][i] = countMin(arr, dp, n, dec, i, i + 1)

        # After considering once by
        # decreasing sequence, now try
        # for increasing sequence.
        else:
            dp[dec][inc][i] = min(countMin(arr, dp, n, dec, i, i + 1), dp[dec][inc][i])

    # If element cannot be part
    # of any of the sequence.
    if dp[dec][inc][i] == -1:
        dp[dec][inc][i] = 1 + countMin(arr, dp, n, dec, inc, i + 1)

    # After considering element as part of increasing and
    # decreasing sequence trying as not part of any of the
    # sequence.
    else:
        dp[dec][inc][i] = min(1 + countMin(arr, dp, n, dec, inc, i + 1), dp[dec][inc][i])

    return dp[dec][inc][i]


# Wrapper Function
def wrapper(arr, n):
    # Adding two number at the end of array, so that
    # increasing and decreasing sequence can be made.
    # MAX - 2 index is assigned INT_MAX for decreasing sequence
    # because/ next number of sequence must be less than it.
    # Similarly, for Increasing sequence INT_MIN is assigned to
    # MAX - 1 index.
    arr[MAX - 2] = 1000000000
    arr[MAX - 1] = -1000000000
    dp = [[[-1 for i in range(MAX)] for i in range(MAX)] for i in range(MAX)]
    return countMin(arr, dp, n, MAX - 2, MAX - 1, 0)


# Driver code
if __name__ == '__main__':
    n = 12
    arr = [7, 8, 1, 2, 4, 6, 3, 5, 2, 1, 8, 7]
    for i in range(MAX):
        arr.append(0)
    print(wrapper(arr, n))

# This code is contributed by sahilshelangia
