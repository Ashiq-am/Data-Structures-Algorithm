# Python3 program to find minimum
# difference between groups of
# highest and lowest sums.
def calculate(a, n):
    # Sorting the whole array.
    a.sort()

    # Generating sum groups.
    s = []
    i = 0
    j = n - 1
    while (i < j):
        s.append((a[i] + a[j]))
        i += 1
        j -= 1

    mini = min(s)
    maxi = max(s)

    return abs(maxi - mini)


# Driver Code
a = [2, 6, 4, 3]
n = len(a)
print(calculate(a, n))


