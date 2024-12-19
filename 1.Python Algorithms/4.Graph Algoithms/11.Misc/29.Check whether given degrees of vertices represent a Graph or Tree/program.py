# Python program to check whether input degree
# sequence is graph or tree
def check(degree, n):
    # Find sum of all degrees
    deg_sum = sum(degree)

    # It is tree if sum is equal to 2(n-1)
    if (2 * (n - 1) == deg_sum):
        return True
    else:
        return False


# main
n = 5
degree = [2, 3, 1, 1, 1]
if (check(degree, n)):
    print("Tree")
else:
    print("Graph")
