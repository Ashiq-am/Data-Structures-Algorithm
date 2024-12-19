# Efficient Python3 program to find maximum
# difference between frequency of any two
# elements such that element with greater
# frequency is also greater in value.

# Return the maximum difference between
# frequencies of any two elements such that
# element with greater frequency is also
# greater in value.
def maxdiff(arr, n):
    freq = {}
    dist = [0] * n

    # Finding the frequency of each element.
    j = 0
    for i in range(n):
        if (arr[i] not in freq):
            dist[j] = arr[i]
            j += 1
            freq[arr[i]] = 0
        if (arr[i] in freq):
            freq[arr[i]] += 1
    dist = dist[:j]

    # Sorting the distinct element
    dist.sort()
    min_freq = n + 1

    # Iterate through all sorted distinct elements.
    # For each distinct element, maintaining the
    # element with minimum frequency than that
    # element and also finding the maximum
    # frequency difference
    ans = 0
    for i in range(j):
        cur_freq = freq[dist[i]]
        ans = max(ans, cur_freq - min_freq)
        min_freq = min(min_freq, cur_freq)

    return ans


# Driven Program
arr = [3, 1, 3, 2, 3, 2]
n = len(arr)

print(maxdiff(arr, n))
