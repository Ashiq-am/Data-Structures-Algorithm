# Python 3 implementation of above approach
n = 7


def minheapify(a, index):
    small = index
    l = 2 * index + 1
    r = 2 * index + 2

    if (l < n and a[l] < a[small]):
        small = l

    if (r < n and a[r] < a[small]):
        small = r

    if (small != index):
        (a[small], a[index]) = (a[index], a[small])
        minheapify(a, small)


# Driver Code
i = 0
k1 = 3
k2 = 6

a = [20, 8, 22, 4, 12, 10, 14]
ans = 0

for i in range((n // 2) - 1, -1, -1):
    minheapify(a, i)

# decreasing value by 1 because we want
# min heapifying k times and it starts
# from 0 so we have to decrease it 1 time
k1 -= 1
k2 -= 1

# Step 1: Do extract minimum k1 times
# (This step takes O(K1 Log n) time)
for i in range(0, k1 + 1):
    a[0] = a[n - 1]
    n -= 1
    minheapify(a, 0)

# Step 2: Do extract minimum k2 – k1 – 1 times and
# sum all extracted elements.
# (This step takes O ((K2 – k1) * Log n) time)*/
for i in range(k1 + 1, k2):
    ans += a[0]
    a[0] = a[n - 1]
    n -= 1
    minheapify(a, 0)

print(ans)
