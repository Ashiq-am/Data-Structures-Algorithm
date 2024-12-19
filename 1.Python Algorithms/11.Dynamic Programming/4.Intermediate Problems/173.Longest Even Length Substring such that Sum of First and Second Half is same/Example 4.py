# A O(n^2) time and O(n) extra
# space solution
def findLength(st, n):
    # To store cumulative total from
    # first digit to nth digit
    total = [0] * (n + 1)

    # Store cumulative total of digits
    # from first to last digit
    for i in range(1, n + 1):
        # convert chars to int
        total[i] = (total[i - 1] +
                    int(st[i - 1]) - int('0'))

    ans = 0  # initialize result

    # consider all even length
    # substings one by one
    l = 2
    while (l <= n):

        for i in range(n - l + 1):

            j = i + l - 1

            # total of first and second half
            # is same than update ans
            if (total[i + int(l / 2)] -
                    total[i] == total[i + l] -
                    total[i + int(l / 2)]):
                ans = max(ans, l)
        l = l + 2

    return ans


# Driver Code
st = "123123"
print("Length of the substring is",
      findLength(st, len(st)))
