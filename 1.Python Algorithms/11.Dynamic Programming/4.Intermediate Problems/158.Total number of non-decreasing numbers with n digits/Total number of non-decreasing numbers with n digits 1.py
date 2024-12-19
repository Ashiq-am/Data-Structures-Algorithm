# python program to count non-decreasing
# number with n digits

def countNonDecreasing(n):
    N = 10

    # Compute value of N*(N+1)/2*(N+2)/3
    # * ....*(N+n-1)/n
    count = 1
    for i in range(1, n + 1):
        count = int(count * (N + i - 1))
        count = int(count / i)

    return count


# Driver program
n = 3
print(countNonDecreasing(n))


