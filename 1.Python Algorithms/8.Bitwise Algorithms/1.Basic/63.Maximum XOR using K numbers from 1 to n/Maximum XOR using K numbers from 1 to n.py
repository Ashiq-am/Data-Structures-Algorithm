# Python3 code to find max xor sum
# of 1 to n using atmost k numbers

# To return max xor sum of 1 to n
# using at most k numbers
def maxXorSum(n, k):
    # If k is 1 then maximum
    # possible sum is n
    if k == 1:
        return n

    # Finding number greater than
    # or equal to n with most significant
    # bit same as n. For example, if n is
    # 4, result is 7. If n is 5 or 6, result
    # is 7
    res = 1
    while res <= n:
        res <<= 1

    # Return res - 1 which denotes
    # a number with all bits set to 1
    return res - 1


# Driver code
n = 4
k = 3
print(maxXorSum(n, k))

# This code is contributed by Abhishek Sharma44.
