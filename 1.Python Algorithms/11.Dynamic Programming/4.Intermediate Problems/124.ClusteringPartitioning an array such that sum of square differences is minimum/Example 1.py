# Python3 program to find minimum
# cost k partitions of array.

# Initialize answer as infinite.
inf = 1000000000
ans = inf


# function to generate all possible answers.
# and compute minimum of all costs.
# i --> is index of previous partition
# par --> is current number of partitions
# a[] and n --> Input array and its size
# current_ans --> Cost of partitions made so far.
def solve(i, par, a, n, k, current_ans):
    # If number of partitions is more than k
    if (par > k):
        return 0

    # If we have mad k partitions and
    # have reached last element
    global ans
    if (par == k and i == n - 1):
        ans = min(ans, current_ans)
        return 0

    # 1) Partition array at different points
    # 2) For every point, increase count of
    # partitions, "par" by 1.
    # 3) Before recursive call, add cost of
    # the partition to current_ans
    for j in range(i + 1, n):
        solve(j, par + 1, a, n, k, current_ans +
              (a[j] - a[i + 1]) * (a[j] - a[i + 1]))


# Driver code
k = 2
a = [1, 5, 8, 10]
n = len(a)
solve(-1, 0, a, n, k, 0)
print(ans)
