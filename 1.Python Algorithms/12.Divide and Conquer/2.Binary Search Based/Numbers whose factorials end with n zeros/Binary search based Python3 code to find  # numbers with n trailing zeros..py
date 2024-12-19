# Binary search based Python3 code to find
# numbers with n trailing zeros.

# Function to calculate trailing zeros
def trailingZeroes(n):
    cnt = 0
    while n > 0:
        n = int(n / 5)
        cnt += n
    return cnt


def binarySearch(n):
    low = 0
    high = 1e6  # range of numbers

    # binary search for first number with
    # n trailing zeros
    while low < high:
        mid = int((low + high) / 2)
        count = trailingZeroes(mid)
        if count < n:
            low = mid + 1
        else:
            high = mid

        # Print all numbers after low with n
    # trailing zeros.
    result = list()
    while trailingZeroes(low) == n:
        result.append(low)
        low += 1

    # Print result
    for i in range(len(result)):
        print(result[i], end=" ")

    # Driver code


n = 2
binarySearch(n)

# This code is contributed by "Sharad_Bhardwaj".
