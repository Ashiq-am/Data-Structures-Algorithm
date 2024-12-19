# Python3 program for Painting
# Fence Algorithm

# Returns count of ways to color
# k posts using k colors
def countWays(n, k):
    # There are k ways to color first post
    total = k
    mod = 1000000007

    # There are 0 ways for single post to
    # violate (same color_ and k ways to
    # not violate (different color)
    same, diff = 0, k

    # Fill for 2 posts onwards
    for i in range(2, n + 1):
        # Current same is same as
        # previous diff
        same = diff

        # We always have k-1 choices
        # for next post
        diff = total * (k - 1)
        diff = diff % mod

        # Total choices till i.
        total = (same + diff) % mod

    return total


# Driver code
if __name__ == "__main__":
    n, k = 3, 2
    print(countWays(n, k))
