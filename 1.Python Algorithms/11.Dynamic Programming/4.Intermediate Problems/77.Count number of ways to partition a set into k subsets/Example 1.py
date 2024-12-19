# A Python3 program to count number
# of partitions of a set with n
# elements into k subsets

# Returns count of different partitions
# of n elements in k subsets
def countP(n, k):
    # Base cases
    if (n == 0 or k == 0 or k > n):
        return 0
    if (k == 1 or k == n):
        return 1

    # S(n+1, k) = k*S(n, k) + S(n, k-1)
    return (k * countP(n - 1, k) +
            countP(n - 1, k - 1))


# Driver Code
if __name__ == "__main__":
    print(countP(3, 2))
